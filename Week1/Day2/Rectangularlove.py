def range(p1, l1, p2, l2):
    
    maxsp = max(p1, p2)
    minep = min(p1 + l1, p2 + l2)

    if maxsp >= minep:
        return (None, None)

  
    overlap_length = minep - maxsp

    return (maxsp, overlap_length)


def find_rectangular_overlap(rect1, rect2):
    
    startPoint_x, overlapWidth  = range(rect1['left_x'],
                                        rect1['width'],
                                        rect2['left_x'],
                                        rect2['width'])
    startPoint_y, overlapHeight = range(rect1['bottom_y'],
                                        rect1['height'],
                                        rect2['bottom_y'],
                                        rect2['height'])

    
    if not overlapWidth or not overlapHeight:
        return {
            'left_x'   : None,
            'bottom_y' : None,
            'width'    : None,
            'height'   : None,
        }

    return {
        'left_x'   : startPoint_x,
        'bottom_y' : startPoint_y,
        'width'    : overlapWidth,
        'height'   : overlapHeight,
    }





