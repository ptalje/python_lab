def tap_element_by_xpath(driver, xpath):
    # In some cases, the webdriver click() operation didn't do the trick. This is an alternate solution
    element = driver.find_element_by_xpath(xpath)
    actions = TouchAction(driver)
    actions.tap(element).perform()
    
def screen_swipe(driver, from_y, to_y, from_x=0, to_x=0, show_debug=False):
    # Perform a screen swipe from coordinates X,Y to X,Y
    # e.g. from_y=400, to_y=200 scroll up 200px
    actions = TouchAction(driver)
    if show_debug:
        print('Scrolling from coordinates X,Y: {},{} to X,Y: {},{}'.format(from_x, from_y, to_x, to_y))
    actions.press(x=from_x, y=from_y).wait(500).move_to(x=to_x, y=to_y).release().perform()
    
 def scroll_to_element_by_xpath(driver, xpath):
    min_y = 200
    sleep(0.5)
    element = driver.find_element_by_xpath(xpath)
    bounds = element.get_attribute('rect')  # {"y":47,"x":0,"width":44,"height":44}
    y = eval(bounds)['y']
    low_hundred = int(y / 100) * 100  # round lowest y coordinate down to nearest 100, e.g. 572 -> 500
    from_y = max(low_hundred, min_y)  # avoid using top coordinates
    screen_swipe(driver, from_y=from_y, to_y=min_y)

    
 def calculate_slider_coordinates(driver, xpath, target_value):
    # When swiping the equalizer sliders, one have to start swiping from the current position.
    # This function calculates the current x,y coordinates based on slider value
    # and calculates the target x,y coordinates for wanted slider value
    # The reason to do it like this is since I could not just send in a target value to the element

    elem = driver.find_element_by_xpath(xpath)
    curr_val = int(common.convert_percentage_value(elem.get_attribute('value')))
    x, y, w, h = common.get_dimensions_of_element_by_xpath(driver, xpath)

    # To handle end coordinates better, subtract/add some pixels from ends
    pixel_threshold = 5
    y = y + pixel_threshold
    h = h - 2 * pixel_threshold  # since we add pixels before, we need to subtract the added first, then again
    mid_x = x + int(w/2)
    curr_slider_pos = y + int(h * (100 - curr_val) / 100)
    target_slider_pos = y + int(h * (100 - target_value) / 100)
    return curr_slider_pos, target_slider_pos, mid_x
