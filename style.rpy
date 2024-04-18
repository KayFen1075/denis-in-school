style say_dialogue_pixel:
    properties gui.text_properties("dialogue")
  
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    
    adjust_spacing False
    font "fonts/ice_pixel-7.ttf"
    size 60

# Стили пиксельного Макса 
style style_pm_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pm/textbox.png", xalign=0.5, yalign=1.0)
style style_pm_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#125e28", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pm_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/Comic Sans MS Pixel.ttf"
    size 50

# Стили пиксельного Саши 
style style_ps_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pm/textbox.png", xalign=0.5, yalign=1.0)
style style_ps_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#231968", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_ps_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 75
    
    adjust_spacing False
    font "fonts/small_pixel-7.ttf"
    size 50

# Стили пиксельного Дениса 
style style_pd_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pm/textbox.png", xalign=0.5, yalign=1.0)
style style_pd_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 12
    
    outlines [(2, "#500505", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pd_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/ComicoroRu_0.ttf"
    size 60

# Стили пиксельного Кирилла 
style style_pk_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pm/textbox.png", xalign=0.5, yalign=1.0)
style style_pk_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#541250", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pk_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/Undertale-Battle-Font.ttf"
    size 50

# Стили пиксельного Юй 
style style_pu_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pm/textbox.png", xalign=0.5, yalign=1.0)
style style_pu_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#5b064e", 0, 0)]
    font "fonts/name.ttf"
    size 60
style style_pu_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1100
    ypos 0.5
    
    adjust_spacing False
    font "fonts/lightpixel_7.ttf"
    size 30




