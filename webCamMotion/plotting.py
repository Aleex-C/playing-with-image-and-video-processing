from video_capture import df

from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource
from bokeh.models.formatters import DatetimeTickFormatter

df["start_string"]=df["start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["end_string"]=df["end"].dt.strftime("%Y-%m-%d %H:%M:%S")
cds = ColumnDataSource(df)

p = figure(x_axis_type='datetime', height=200, width=1500, sizing_mode='stretch_width',title="Motion movements times")
p.yaxis.minor_tick_line_color=None
p.yaxis.ticker.desired_num_ticks=1
p.xaxis.axis_label='time'
p.xaxis.formatter = DatetimeTickFormatter(days="%d-%b-%Y", hours="%H:%M", seconds="%M:%S")

hover = HoverTool(tooltips=[("Start", "@start_string"), ("End", "@end_string")])
p.add_tools(hover)
q=p.quad(left="start", right="end", bottom=0, top=1, color="black", source=cds)

output_file("Motion1.html")
show(p)