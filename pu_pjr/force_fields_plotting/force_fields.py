from matplotlib import pyplot as plt

from . import utils

def get_field_data(
    field: utils.Fields, points: list[float], **kwargs
) -> list[float]:
    """Get the values for some points in a field"""
    if field == utils.Fields.LJ_CUT:
        # print("lj/cut field")
        return utils.lj_cut(points, **kwargs)
    else:
        raise NotImplementedError(f'Field {field} not implemented')
    
def plot_field(
    field: utils.Fields = utils.Fields.LJ_CUT, 
    points: list[float] = utils.create_range(), 
    **kwargs
) -> None:
    """Plot a field"""

    x = points
    y = get_field_data(field, points, **kwargs)
    # print(x, len(x))
    # print(y)

    plt.plot(x, y, 'o-')
    plt.show(block=True)