zip = () ->
  lengthArray = (arr.length for arr in arguments)
  length = Math.min(lengthArray...)
  for i in [0...length]
      arr[i] for arr in arguments


class Chordata
    constructor: (@el) ->
        @el = el
        @context = el.getContext('2d')
        @PAD_LEFT = 25
        @PAD_TOP = 17
        @BAR_WIDTH = 30
        @COLOR_STRING = 'black'
        @COLOR_MSTRING = '#FFA62F'
        @COLOR_BAR = 'darkgrey'
        @COLOR_INLAY = '#E8E8E8'

    line: (start, end, color, width=2) ->
        @context.beginPath()
        @context.moveTo(start[0], start[1])
        @context.lineTo(end[0], end[1])
        @context.lineWidth = width
        @context.strokeStyle = color
        @context.stroke()
        @context.closePath()

    circle: (x, y, radius, fill='black') ->
        @context.beginPath()
        @context.arc(x, y, radius, 0, 2 * Math.PI, false)
        @context.fillStyle = fill
        @context.fill()
        @context.closePath()

    render_chord: (name, pattern, strings) ->
        patt = (one for one in pattern when one > 0)
        patt.sort((a,b) -> a-b)
        start = if patt.length then (if patt[0]==1 then 1 else patt[0]-1) else 1
        end = if patt.length then patt[patt.length-1]+2 else 5

        bars = [start...end]
        #set canvas width (it's being truncated)
        $(@el).attr('width', (bars.length+1)*@BAR_WIDTH)
        $(@el).css('width: ' + bars.length+1)*@BAR_WIDTH + 'px'
        $(@el).attr('height', @PAD_TOP*(strings.length+2))
        $(@el).css('height: ' + @PAD_TOP*(strings.length+2) + 'px')

        #bars
        for b,i in bars
            @line(
                start=[@PAD_LEFT+(i*@BAR_WIDTH), @PAD_TOP]
                end=[@PAD_LEFT+(i*@BAR_WIDTH), @PAD_TOP*strings.length],
                color=@COLOR_BAR
            )

            @context.fillStyle = @COLOR_STRING
            @context.fillText(b, @PAD_LEFT-@BAR_WIDTH/1.5+@BAR_WIDTH*(i+1), @PAD_TOP-@PAD_TOP/2)

            if b in [3,5,7,10,12,15,17,19,21,24]
                @circle((@PAD_LEFT-@BAR_WIDTH/2)+@BAR_WIDTH*(b-bars[0]+1),
                        @PAD_TOP*strings.length/2+@PAD_TOP/2,
                        radius=3.5, fill=@COLOR_INLAY)

        for [one,string,i] in zip(pattern, strings, [0...strings.length + 1])
            muted = if one < 0 then true else false
            color = if muted then @COLOR_MSTRING else @COLOR_STRING

            #strings
            @line(
                start=[@PAD_LEFT, @PAD_TOP*(i+1)],
                end=[(bars.length+1)*@BAR_WIDTH, @PAD_TOP*(i+1)],
                color=color
            )

            #string names
            @context.fillStyle = color
            @context.fillText((if muted then 'X' else string), @PAD_LEFT/2, @PAD_TOP*(i+1)+2)

            #fingers
            if one > 0
                @circle((@PAD_LEFT-@BAR_WIDTH/2)+@BAR_WIDTH*(one-bars[0]+1), @PAD_TOP*(i+1), 5.5)

        @context.fillStyle = @COLOR_STRING
        @context.fillText(name, @PAD_LEFT+@BAR_WIDTH*bars.length/2.5, @PAD_TOP*(strings.length+1.5))

render_chord = (name, pattern, strings, cid) ->
    canvas = document.getElementById(cid)
    c = new Chordata(canvas)
    pattern = pattern.reverse()
    c.render_chord(name, pattern, strings)


$ ->
    if RESULTS?
        strings = STRINGS.reverse()
        for [name, pattern, same_pattern],i in RESULTS
            render_chord(name, pattern, strings, "c#{i}")
            for [sname, spattern],si in same_pattern
                render_chord(sname, spattern, strings, "cs#{si}c#{i}")
        $('a.with_same_pattern').on('click', () ->
            $(this).siblings('.same_pattern').toggle()
            return false
        )
        $('.same_pattern').hide()
