##############################################################################
    # You don't need the character template to use the Portrait engine,
    # that's below the next divider.
    # However, this code does make it easier to keep dialogue formatted
    # consistently between speakers.
    
    # If you copy the way I format my Characters in the third section of this
    # file though, you *will* need this section.

init python:
    # Character template
    def CharTemplate(name=None, quote=True, mode=None, file=None, speaker=None, **args):
        if quote:
            return Character(name, what_prefix=u"“", what_suffix="”", who_prefix=u"【", who_suffix="】", ctc="continimg", ctc_pause="continimg", ctc_timedpause=Null(), kind=mode, callback=text_effect(file, speaker), **args)
        else:
            return Character(name, ctc="continimg", ctc_pause="continimg", ctc_timedpause=Null(), kind=mode, **args)
    
    # Text blip and speaker set
    def text_effect(file, speaker, event, **args):
        if event == "show_done":
            pass
            if file and _preferences.text_cps != 0:
                renpy.music.play(file, channel="text")
        elif event == "slow_done" or event == "end":
            speaking = None
            renpy.music.stop(channel="text")
        renpy.invoke_in_new_context(speaker_curry(speaker, event))
    text_effect = renpy.curry(text_effect)

    # This is set to the name of the character that is speaking, or
    # None if no character is currently speaking.
    speaking = None
  
    # This callback maintains the speaking variable.
    def speaker_callback(name, event, **kwargs):
        global speaking
        
        if event == "show":
            speaking = name
        elif event == "slow_done":
            speaking = None
        elif event == "end":
            speaking = None
  
    # Curried form of the same.
    speaker_curry = renpy.curry(speaker_callback)
  
##############################################################################
    # This is the Portrait System! You copy this into your own game in wherever
    # you think it's best suited.

init python:
    import random
    import math
    class Portrait(renpy.Displayable):
        def __init__(self, image, width=416, eyepos=(0,0), moupos=(0,0), eyesize=(128, 64), mousize=(128, 64), speaker=None, **kwargs):
            super(Portrait, self).__init__(**kwargs)      
            self.image = ("%s" % image)
            self.portrait_width = width
            self.eyes = eyepos + eyesize
            self.mouth = moupos + mousize
            
            self.speaker = speaker
            self.bt()
            
        def bt(self, **kwargs):
            self.blink_time = random.choice([3, 4, 4, 4, 5, 5, 5, 6])

        def render(self, width, height, st, at):
            # This is the base portrait displayable
            portrait = im.Crop(self.image, (0, 0, self.portrait_width, 640))
            # This is the render of the base portrait displayable.
            portrait_render = renpy.render(portrait, self.portrait_width, 640, st, at)
            
            # Now we're going to render the eyes
            # The reason why we're using a DynamicDisplayable here is that it forces us to rerender the eyes later.
            eye_render = renpy.render(DynamicDisplayable(self.redraw_eyes), self.eyes[2], self.eyes[3], st, at)
            portrait_render.blit(eye_render, (self.eyes[0], self.eyes[1]))
            # This is a render of the mouth, and it follows the same pattern as the eyes
            global speaking
            if speaking == self.speaker and self.speaker != None:
                mouth_render = renpy.render(DynamicDisplayable(self.redraw_mouth), self.mouth[2], self.mouth[3], st, at)
                portrait_render.blit(mouth_render, (self.mouth[0], self.mouth[1]))

            # Return the render.
            flatten_portrait = renpy.render(Flatten(portrait), self.portrait_width, 640, st, at)
            return flatten_portrait
            
        def redraw_eyes(self, st, at):
            # Set frames
            half_opened = im.Crop(self.image, (self.portrait_width, 0, self.eyes[2], self.eyes[3]))
            closed = im.Crop(self.image, (self.portrait_width, self.eyes[3], self.eyes[2], self.eyes[3]))
            # Draw frames as per this timing
            p = self.blink_time
            time = st % (p + .4)
            if p < time < (p + .1):
                return half_opened, 0.05
            elif (p + .1) < time < (p + .2):
                return closed, 0.05
            elif (p + .2) < time < (p + .3):
                return half_opened, 0.05
            elif (p + .3) < time < (p + .4):
                self.bt()
                return Null(), 0.05
            else:
                return Null(), 0.05
        
        def redraw_mouth(self, st, at):
            # Set frames
            mouth_y_orign = self.eyes[3]*2 + 32
            half_opened = im.Crop(self.image, (self.portrait_width, mouth_y_orign, self.mouth[2], self.mouth[3]))
            opened = im.Crop(self.image, (self.portrait_width, mouth_y_orign+self.mouth[3], self.mouth[2], self.mouth[3]))
            # Draw frames as per this timing
            time = st % .4
            if time < .1:
                return half_opened, 0.1
            elif time < .2:
                return opened, 0.1
            elif time < .3:
                return half_opened, 0.1
            else:
                return Null(), 0.1 
    
    def PortraitStrip(st, at, image, width, frames):
        f = min([frames, math.trunc(st * 10)])
        frame = im.Crop("%s" % image, (f * width, 0, width, 640))
        return frame, .1
            
##############################################################################
    # The following code is only for the demo. You don't need to include this,
    # however you can use it to learn from.

    # Characters
    #june    = CharTemplate("June",      file="vb_high2.ogg",    speaker="june")
    #clover  = CharTemplate("Clover",    file="vb_high3.ogg",    speaker="clover")
    #lotus   = CharTemplate("Lotus",     file="vb_high1.ogg",    speaker="lotus")
    #nv      = CharTemplate(quote=False, mode=nvl)

#init:
    # Portraits
    
    # June
    #image june idle         = Portrait("june/idle.png",         eyepos=(144, 192),  moupos=(144,256), speaker="june")
    #image june concern      = Portrait("june/concern.png",      eyepos=(144, 208),  moupos=(144,272), speaker="june")
    
    # Clover
    #image clover concern    = Portrait("clover/concern.png",    eyepos=(160, 240),  moupos=(144,304), speaker="clover")
    #image clover shock      = Portrait("clover/shock.png",      eyepos=(144, 224),  moupos=(144,288), speaker="clover")
    #image clover anger      = Portrait("clover/anger.png",      eyepos=(128, 240),  moupos=(128,304), speaker="clover")
    #image clover point:
    #    DynamicDisplayable(PortraitStrip, "clover/point_start.png", 480, 7)
    #    pause 0.8
    #    Portrait("clover/point.png", moupos=(128,320), speaker="clover")
    #image clover point2 = Portrait("clover/point.png", moupos=(128,320), speaker="clover")

    # Lotus
    #image lotus thought     = Portrait("lotus/thought.png",     eyepos=(144, 192),  moupos=(144,256), speaker="lotus")
    #image lotus handwave    = Flatten(LiveComposite((416, 640),
    #    (0, 0), Portrait("lotus/handwave.png", eyepos=(128,192), moupos=(128,256), speaker="lotus"),
    #    (0, 0), "lotus hw_hand",))
    #image lotus hw_hand:
    #    DynamicDisplayable(PortraitStrip, "lotus/handwave_hand.png", 416, 7)
    #    pause 3.8
    #    repeat   
