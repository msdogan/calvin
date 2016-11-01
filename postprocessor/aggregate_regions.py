import pandas as pd

# run this only after postprocess.py
# this appends columns to the shortage cost/volume files

sc = pd.read_csv('shortage_cost.csv', index_col=0, parse_dates=True)
sv = pd.read_csv('shortage_volume.csv', index_col=0, parse_dates=True)
regions = pd.read_csv('demand_nodes.csv', index_col = 0)

for R in regions.region.unique():
  for t in regions.type.unique():
    links = regions.index[(regions.region == R) & (regions.type == t)]
    sc['%s_%s' % (R,t)] = sc[links].sum(axis=1)
    sv['%s_%s' % (R,t)] = sv[links].sum(axis=1)

sc.to_csv('shortage_cost.csv')
sv.to_csv('shortage_volume.csv')
