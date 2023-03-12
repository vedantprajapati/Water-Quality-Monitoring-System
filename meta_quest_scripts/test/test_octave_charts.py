from ..octave_charts import draw_octave

def test_draw_octave():
    args = [[10, 0.5, 1000, 255, 0, 0, True], [10, 0.5, 1000, 0, 255, 0, True]]

    commands = [draw_octave(*arg) for arg in args]
    desired = [
        ('octave-cli octave_scripts/plot_pad.m 10 0.5 1000 255 0 0'),
        ('octave-cli octave_scripts/plot_pad.m 10 0.5 1000 0 255 0'),
    ]
    assert all([command[0] == desired_command for command, desired_command in zip(commands, desired)])