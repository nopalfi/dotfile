# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401

mod = "mod4"                                     # Sets mod key to SUPER/WINDOWS
myTerm = "kitty -e"                                 # My terminal of choice
browser = "brave"                               # My browser choice
home = os.path.expanduser("~")

keys = [
         ### The essentials
         Key([mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches My Terminal'
             ),
         Key([mod], "r",
             lazy.spawncmd(),
             desc='Launch spawncmd'
             ),
         Key([mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key([mod, "shift"], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key([mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
         Key([mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         ### Switch focus to specific monitor (out of three)
         Key([mod], "w",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "e",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         ### Switch focus of monitors
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         ### Treetab controls
          Key([mod, "shift"], "h",
             lazy.layout.move_left(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "shift"], "l",
             lazy.layout.move_right(),
             desc='Move down a section in treetab'
             ),
         ### Window controls
         Key([mod], "j",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key([mod], "k",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key([mod, "shift"], "j",
             lazy.layout.shuffle_down(),
             lazy.layout.section_down(), desc='Move windows down in current stack'
             ),
         Key([mod, "shift"], "k",
             lazy.layout.shuffle_up(),
             lazy.layout.section_up(),
             desc='Move windows up in current stack'
             ),
         Key([mod], "h",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key([mod], "l",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key([mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key([mod], "Prior",
             lazy.window.toggle_minimize(),
             desc='minimize a window'
             ),
         Key([mod], "Next",
             lazy.window.toggle_maximize(),
             desc='maximize a window'
             ),
        Key([mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key([mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key([mod], "f",
             lazy.window.toggle_fullscreen(),
             desc='toggle fullscreen'
             ),
         ### Stack controls
         Key([mod, "shift"], "Tab",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
          Key([mod], "space",
             lazy.group.next_window(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key([mod, "shift"], "space",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),
         ### Application shortcut
         Key([mod, "shift"], "b",
             lazy.spawn(browser),
             desc='Launch a browser'
             ),
         Key([mod, "control", "shift"], "q",
             lazy.spawn(myTerm + " vim " + home +"/.config/qtile/config.py"),
             desc='Launch Terminal and Edit Qtile config in vim',
             ),
         Key([mod, "shift"], "e",
             lazy.spawn(myTerm + " ranger"),
             desc='Launch ranger file manager',
             ),
         ### Fn key shortcut
         Key([], "XF86AudioRaiseVolume",
             lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
             desc='Raise Pulseaudio Volume'
             ),
         Key([], "XF86AudioLowerVolume",
             lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
             desc='Raise Pulseaudio Volume'
             ),
         Key([], "XF86AudioMute",
             lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
             desc='Raise Pulseaudio Volume'
             ),
         Key([], "XF86MonBrightnessUp",
             lazy.spawn("brightnessctl s 5%+"),
             desc='Set monitor brightness up 5%'
             ),
         Key([], "XF86MonBrightnessDown",
             lazy.spawn("brightnessctl s 5%-"),
             desc='Set monitor brightness down 5%'
             ),
         ### CTRL Sound key Shortcut for regular keyboard
         Key(["control"], "F12",
             lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%"),
             desc='Raise Pulseaudio Volume'
             ),
         Key(["control"], "F11",
             lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%"),
             desc='Raise Pulseaudio Volume'
             ),
         Key(["control"], "F10",
             lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle"),
             desc='Raise Pulseaudio Volume'
             ),
         ### CTRL Brighness shortcut key for regular keyboard
         Key(["control"], "F5", 
             lazy.spawn("brightnessctl s 10%-"),
             desc='Raise monitor brightness'
             ),
         Key(["control"], "F6",
             lazy.spawn("brightnessctl s +10%"),
             desc='Lower Monitor brightness'
             ),
         ### Flameshot configuration
         Key([], "Print",
             lazy.spawn("flameshot gui"),
             desc='Open Flameshot gui'
             ),
         Key([mod], "Print",
             lazy.spawn("flameshot full -c"),
             desc='Screenshot screen and copy to clipboard'
             ),
         Key([mod, "shift"], "Print",
             lazy.spawn("flameshot gui -g"),
             desc='Screenshot selected area'
             ),
         Key(["shift"], "Print",
             lazy.spawn("flameshot full -c -p "+ home +"/Pictures"),
             desc='Screenshot screen, copy to clipboard, and save it in /Picture'
             )
         ]

group_names = [("💻", {'layout': 'monadtall'}),
               ("🌏", {'layout': 'max'}),
               ("📂", {'layout': 'monadtall'}),
               ("⚙️", {'layout': 'floating'}),
               ("🔗", {'layout': 'treetab'}),
               ("🎮", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group



layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "dddede",
                "border_normal": "232122"
                }

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
    layout.TreeTab(
         font = "Ubuntu",
         fontsize = 10,
         sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
         section_fontsize = 10,
         border_width = 2,
         bg_color = "1c1f24",
         active_bg = "c678dd",
         active_fg = "000000",
         inactive_bg = "a9a1e1",
         inactive_fg = "1c1f24",
         padding_left = 0,
         padding_x = 0,
         padding_y = 5,
         section_top = 10,
         section_bottom = 20,
         level_shift = 8,
         vspace = 3,
         panel_width = 130
         ),
    layout.Floating(**layout_theme)
]

colors = [["#2a3132", "#2a3132"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#f1f1f2", "#f1f1f2"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#14281d", "#14281d"], # border line color for 'other tabs' and color for 'odd widgets'
          ["#6e633d", "#6e633d"], # color for the 'even widgets'
          ["#f1f1f2", "#f1f1f2"], # window name
          ["#ecbbfb", "#ecbbfb"]] # backbround for inactive screens

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Ubuntu Mono",
    fontsize = 12,
    padding = 2,
    background=colors[2]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
              widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 9,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = colors[7],
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Prompt(
                       prompt = prompt,
                       font = "Ubuntu Mono",
                       padding = 10,
                       foreground = colors[2],
                       background = colors[4]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 40,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.WindowName(
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Systray(
                       background = colors[0],
                       padding = 5
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 5,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.Sep(
                       linewidth = 0,
                       padding = 3,
                       foreground = colors[2],
                       background = colors[0]
                       ),
              widget.BatteryIcon(
                       background = colors[0],
                       foreground = colors[6],
                       padding = 3,
                       fontsize = 37,
                       update_interval = 60
                      ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       fontsize = 37
                       ),
             widget.CPU(
                       format = '💻 {load_percent}%',
                       update_interval = 1.0,
                       forground = colors[2],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bashtop')},
                       padding = 0
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       fontsize = 37
                       ),
             widget.Net(
                       interface = 'wlp3s0',
                       format = '{down} ↓↑ {up}',
                       forground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.TextBox(
                       text = " 🖬",
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0,
                       fontsize = 14
                       ),
              widget.Memory(
                       foreground = colors[2],
                       background = colors[0],
                       mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e bashtop')},
                       padding = 0
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[6],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.CurrentLayoutIcon(
                       custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                       foreground = colors[6],
                       background = colors[0],
                       padding = 0,
                       scale = 0.7
                       ),
              widget.CurrentLayout(
                       foreground = colors[2],
                       background = colors[0],
                       padding = 0
                       ),
              widget.TextBox(
                       text = '|',
                       background = colors[0],
                       foreground = colors[2],
                       padding = 0,
                       fontsize = 37
                       ),
              widget.Clock(
                       foreground = colors[2],
                       background = colors[0],
                       format = "%A, %d-%B %H:%M "
                       ),
              ]
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    del widgets_screen1[7:8]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=18)),
            Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=18)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=18))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = False
bring_front_click = True
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    Match(wm_class='Steam'),
])
auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
