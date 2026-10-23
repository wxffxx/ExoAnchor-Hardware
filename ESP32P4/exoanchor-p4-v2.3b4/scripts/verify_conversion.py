"""Compare the current PCB and freshly exported KiCad netlist to source endpoints.

Export validation/kicad-netlist.xml with kicad-cli before running this script.
This is a conversion-parity check, not ERC/DRC or a manufacturing approval.
"""
import json,collections,xml.etree.ElementTree as ET,math
from pathlib import Path
from sexp import *
P=Path(__file__).resolve().parents[1]
s=json.loads((P/'validation/source-data.json').read_text());src={c['attrs']['Designator']:c for c in s['components'].values()}
b=parse(P/'KiCad/ExoAnchor_P4_V2.3B4.kicad_pcb')
physical={val(prop(f,'Reference')[2]):f for f in children(b,'footprint') if val(prop(f,'Reference')[2]) in src}
mis=[];checks=0;position=[]
for ref,f in physical.items():
 for pad in children(f,'pad'):
  n=val(pad[1]);net=val(child(pad,'net')[-1]) if child(pad,'net') else '';exp=src[ref]['nets'].get(n,'');checks+=1
  if net!=exp:mis.append([ref,n,exp,net])
 transform=child(f,'transform');xy=list(map(float,child(transform,'translate')[1:3]));r=src[ref]['record'];err=math.hypot(xy[0]-r[4]*.0254-40,xy[1]+r[5]*.0254-20)
 if err>.001:position.append([ref,err])
x=ET.parse(P/'validation/kicad-netlist.xml').getroot();kc=collections.defaultdict(set);sc=collections.defaultdict(set)
for net in x.findall('./nets/net'):
 for n in net.findall('node'):
  if n.get('ref') in src:kc[net.get('name')].add((n.get('ref'),n.get('pin')))
for ref,c in src.items():
 for num,net in c['nets'].items():
  if net:sc[net].add((ref,num))
rev={frozenset(v):k for k,v in kc.items()};bad=[]
for net,nodes in sc.items():
 if frozenset(nodes) not in rev:
  overlaps=sorted([(len(nodes&v),k,len(v),sorted(nodes-v),sorted(v-nodes)) for k,v in kc.items() if nodes&v],reverse=True)[:3];bad.append({'source':net,'nodes':len(nodes),'closest':overlaps})
schrefs={n.get('ref') for n in x.findall('./components/comp')}
missing_pads=[]
for ref,c in src.items():
 actual={val(p[1]) for p in children(physical[ref],'pad')} if ref in physical else set()
 if actual!=set(c['nets']):missing_pads.append({'ref':ref,'missing':sorted(set(c['nets'])-actual),'extra':sorted(actual-set(c['nets']))})
report={'source_components':len(src),'pcb_components':len(physical),'schematic_components':len(schrefs),'reference_sets_equal':set(src)==set(physical)==schrefs,'pad_checks':checks,'pad_mismatches':mis,'pad_number_set_mismatches':missing_pads,'position_mismatches_over_1um':position,'source_nonempty_nets':len(sc),'matched_net_partitions':len(sc)-len(bad),'net_partition_mismatches':bad,'native_item_counts':dict(collections.Counter(n[0] for n in b if isinstance(n,list)))}
report['pass']=report['reference_sets_equal'] and not (mis or missing_pads or position or bad)
(P/'validation/parity.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:v for k,v in report.items() if k!='net_partition_mismatches'},ensure_ascii=False,indent=2));print('Net mismatches:',len(bad))
raise SystemExit(0 if report['pass'] else 1)
