import pyecharts.options as opts
from pyecharts.charts import MapGlobe
from pyecharts.faker import POPULATION
data = [x for _, x in POPULATION[1:]]
low, high = min(data), max(data)
fig = (
    MapGlobe(init_opts=opts.InitOpts())
    .add_schema()
    .add(
        maptype="china",
        series_name="World Population",
        data_pair=POPULATION[1:],
#         is_map_symbol_show=False,
        is_map_symbol_show=True,  # 显示地图标签，把False改成True,国家名字就显示出来了
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            min_=low,
            max_=high,
            range_text=["max", "min"],
#             is_calculable=False,
#             is_piecewise=False,
            is_calculable=True,
            is_piecewise=True,
            range_color=["lightskyblue", "yellow", "orangered"],
#
        )
    )
)
# d.render_notebook()
fig.render_notebook()
