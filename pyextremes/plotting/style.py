import matplotlib

theme_color = '#454545'
pyextremes_rc = {
    'font.family': 'arial',
    'font.size': 10,
    'text.color': theme_color,
    'axes.edgecolor': theme_color,
    'axes.linewidth': 0.8,
    'axes.grid': True,
    'axes.labelsize': 10,
    'axes.labelweight': 'normal',
    'axes.prop_cycle': matplotlib.cycler(
        'color',
        [
            '#1771F1',
            '#F85C50',
            '#35D073',
            '#FFC11E'
        ]
    ),
    'xtick.major.size': 2,
    'xtick.minor.size': 1,
    'xtick.major.width': 0.8,
    'xtick.minor.width': 0.6,
    'xtick.major.top': True,
    'xtick.major.bottom': True,
    'xtick.minor.top': True,
    'xtick.minor.bottom': True,
    'xtick.color': theme_color,
    'ytick.major.size': 2,
    'ytick.minor.size': 1,
    'ytick.major.width': 0.8,
    'ytick.minor.width': 0.6,
    'ytick.color': theme_color,
    'ytick.major.left': True,
    'ytick.major.right': True,
    'ytick.minor.left': True,
    'ytick.minor.right': True,
    'grid.color': theme_color,
    'grid.linestyle': ':',
    'grid.linewidth': 0.4,
    'grid.alpha': 1.0,
    'legend.frameon': False,
    'legend.edgecolor': theme_color,
    'figure.figsize': (8, 5),
    'figure.dpi': 96
}
