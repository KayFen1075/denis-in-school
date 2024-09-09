style pixel_say_dialogue:
    properties gui.text_properties("dialogue")
  
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    
    adjust_spacing False
    font "fonts/ice_pixel-7.ttf"
    size 60
style pixel_say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#125e28", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60

style error:
    font "fonts/DOTS 6.0.otf"
    yalign 0.5

    xpos 0.5
    ypos 18
style error_name:
    properties gui.text_properties("name", accent=True)
    font "fonts/DOTS 6.0.otf"
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
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

style style_pm_back:
    variant "small"
    ypos 725
style style_pm_label:
    variant "small"
    ypos 50
style style_pm_dialogue:
    variant "small"
    ypos 125

# Стили пиксельного Саши 
style style_ps_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/ps/textbox.png", xalign=0.5, yalign=1.0)
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

style style_ps_back:
    variant "small"
    ypos 725
style style_ps_label:
    variant "small"
    ypos 50
style style_ps_dialogue:
    variant "small"
    ypos 125

# Стили пиксельного Дениса 
style style_pd_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pd/textbox.png", xalign=0.5, yalign=1.0)
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

style style_pd_back:
    variant "small"
    ypos 725
style style_pd_label:
    variant "small"
    ypos 50
style style_pd_dialogue:
    variant "small"
    ypos 125

# Стили пиксельного Кирилла 
style style_pk_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pk/textbox.png", xalign=0.5, yalign=1.0)
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

style style_pk_back:
    variant "small"
    ypos 725
style style_pk_label:
    variant "small"
    ypos 50
style style_pk_dialogue:
    variant "small"
    ypos 125

# Стили пиксельной Юй 
style style_pu_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pu/textboxui.png", xalign=0.5, yalign=1.0)
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

style style_pu_back:
    variant "small"
    ypos 725
style style_pu_label:
    variant "small"
    ypos 50


# Стили пиксельного Санька 
style style_px_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/Born2bSportyFS.otf"

    background Image("gui/personalUI/px/textbox.png", xalign=0.5, yalign=1.0)
style style_px_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#452f0a", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_px_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/Comic Sans MS Pixel.ttf"
    size 50

style style_px_back:
    variant "small"
    ypos 725
style style_px_label:
    variant "small"
    ypos 50
style style_px_dialogue:
    variant "small"
    ypos 125

# Стили пиксельного Бориса 
style style_pb_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pb/textbox.png", xalign=0.5, yalign=1.0)
style style_pb_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#431057", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pb_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/old_pixel-7.ttf"
    size 60

style style_pb_back:
    variant "small"
    ypos 725
style style_pb_label:
    variant "small"
    ypos 50
style style_pb_dialogue:
    variant "small"
    ypos 125

# Стили пиксельной Тянки
style style_pt_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pt/textbox.png", xalign=0.5, yalign=1.0)
style style_pt_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#6b3d5a", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pt_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/ChixaDemibold.ttf"
    size 50

style style_pt_back:
    variant "small"
    ypos 725
style style_pt_label:
    variant "small"
    ypos 50
style style_pt_dialogue:
    variant "small"
    ypos 125

# Стили пиксельного Тараса
style style_pz_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pz/textbox.png", xalign=0.5, yalign=1.0)
style style_pz_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#787223", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pz_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/ChixaDemibold.ttf"
    size 50

style style_pz_back:
    variant "small"
    ypos 725
style style_pz_label:
    variant "small"
    ypos 50
style style_pz_dialogue:
    variant "small"
    ypos 125

# Стили пиксельного Любимого
style style_pl_back:
    xalign 0.1
    xfill True
    ypos 770
    ysize gui.textbox_height
    font "fonts/gialog.ttf"

    background Image("gui/personalUI/pl/textbox.png", xalign=0.5, yalign=1.0)
style style_pl_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

    xpos 0.5
    ypos 18
    
    outlines [(2, "#125e28", 0, 0)]
    font "fonts/name.ttf"
    background "black"
    size 60
style style_pl_dialogue:
    properties gui.text_properties("dialogue")

    xpos 0.5
    xsize 1300
    ypos 80
    
    adjust_spacing False
    font "fonts/Comic Sans MS Pixel.ttf"
    size 50

style style_pl_back:
    variant "small"
    ypos 725
style style_pl_label:
    variant "small"
    ypos 50
style style_pl_dialogue:
    variant "small"
    ypos 125

