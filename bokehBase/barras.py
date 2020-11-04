from bokeh.plotting import figure, output_file, show

output_file('vbar.html')

p = figure(plot_width=500, plot_height=400)
p.vbar(x=[1, 2, 3], width=0.8, bottom=0,
       top=[1.2, 2.5, 3.7], color=["red", "yellow", "green"], alpha=[0.8, 0.3, 0.5])

show(p)