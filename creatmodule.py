# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:19:04 2022

@author: user
"""

import pyecharts.options as opts
from pyecharts import options as opts
from pyecharts.charts import Line,Bar,Grid,Scatter3D,EffectScatter,Pie,WordCloud
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

def Js_line(x_data,y_data,searchvalue):
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
    )
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
    )
    
    c = (
        Line(init_opts=opts.InitOpts(bg_color='rgba(255,255,255,0)'))#background_color
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name="value",
            y_axis=y_data,
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#5175DB"),
            label_opts=opts.LabelOpts(is_show=True, position="top", color="#5175DB"),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", border_color="#5175DB", border_width=6
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"{searchvalue} 每坪均價/萬",
                pos_bottom="15%",
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="#5175DB", font_size=16),
                #title color
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#000"),#x軸label顏色
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#DFDFE3")#x軸colume color
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                position="right",
                axislabel_opts=opts.LabelOpts(margin=20, color="#000"),#y軸labe color
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(width=2, color="#DFDFE3")#右側網格顏色
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#fff"),#y軸line color
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#DFDFE3")#y軸網格顏色
                ),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        
        .dump_options()
    )
    
    return c
def Creat_Pie_rich(x_data,y_data):
    c = (
        Pie()
        .add(
            "",
            [list(z) for z in zip(x_data, y_data)],
            radius=["40%", "55%"],
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "left"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="World"))
        .dump_options()
        
    )
   
    return c
def Creat_WorldCloud(data):
    
    k=(WordCloud(init_opts=opts.InitOpts(width='400px', height='400px'))
    .add(series_name="", data_pair=data, word_size_range=[6,100])
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="交易量熱區", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render_embed()
    
)
    return k


def Forecast_plot(pred_tmp,time_tmp):
    import pyecharts.options as opts
    from pyecharts.charts import Line

    c = (
        Line()
        .add_xaxis(time_tmp)
        .add_yaxis("價格(萬元)", pred_tmp)

        .set_global_opts(title_opts=opts.TitleOpts(title="未來趨勢"))
        .render_embed()
    )
    return c

def Forecast_plot2(address,pred_tmp,time_tmp):
    import pyecharts.options as opts
    from pyecharts.charts import Line
    from pyecharts.faker import Faker
    
    c = (
        Line()
        .add_xaxis(time_tmp)
        .add_yaxis("每坪價格(萬元)", pred_tmp, areastyle_opts=opts.AreaStyleOpts(opacity=0.5))
        
        .set_global_opts(title_opts=opts.TitleOpts(title=address))
        .render_embed()
    )
    return c
def Forecast_js(address,pred_tmp,time_tmp):
    background_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#c86589'}, {offset: 1, color: '#06a7ff'}], false)"
    )
    area_color_js = (
        "new echarts.graphic.LinearGradient(0, 0, 0, 1, "
        "[{offset: 0, color: '#eb64fb'}, {offset: 1, color: '#3fbbff0d'}], false)"
    )
    
    c = (
        Line(init_opts=opts.InitOpts(bg_color='rgba(255,255,255,0)'))#background_color
        .add_xaxis(xaxis_data=time_tmp)
        .add_yaxis(
            series_name="value",
            y_axis=pred_tmp,
            is_smooth=True,
            is_symbol_show=True,
            symbol="circle",
            symbol_size=6,
            linestyle_opts=opts.LineStyleOpts(color="#5175DB"),
            label_opts=opts.LabelOpts(is_show=True, position="top", color="#5175DB"),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red", border_color="#5175DB", border_width=6
            ),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            areastyle_opts=opts.AreaStyleOpts(color=JsCode(area_color_js), opacity=1),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"{address} 每坪均價/萬",
                pos_bottom="15%",
                pos_left="center",
                title_textstyle_opts=opts.TextStyleOpts(color="#5175DB", font_size=16),
                #title color
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                boundary_gap=False,
                axislabel_opts=opts.LabelOpts(margin=30, color="#000"),#x軸label顏色
                axisline_opts=opts.AxisLineOpts(is_show=False),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=25,
                    linestyle_opts=opts.LineStyleOpts(color="#ffffff"),
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#DFDFE3")#x軸colume color
                ),
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                position="right",
                axislabel_opts=opts.LabelOpts(margin=20, color="#000"),#y軸labe color
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(width=2, color="#DFDFE3")#右側網格顏色
                ),
                axistick_opts=opts.AxisTickOpts(
                    is_show=True,
                    length=15,
                    linestyle_opts=opts.LineStyleOpts(color="#fff"),#y軸line color
                ),
                splitline_opts=opts.SplitLineOpts(
                    is_show=True, linestyle_opts=opts.LineStyleOpts(color="#DFDFE3")#y軸網格顏色
                ),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        
        .render_embed()
    )
    
    return c