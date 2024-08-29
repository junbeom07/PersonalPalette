        if s_mean >= 226:
            color_text = "Vivid"
        elif 142 <= s_mean < 226:
            if abs(v_mean - 180) < abs(v_mean - 240) and abs(v_mean - 180) < abs(v_mean - 250):
                color_text = "Deep"
            elif abs(v_mean - 240) < abs(v_mean - 180) and abs(v_mean - 240) < abs(v_mean - 250):
                color_text = "Strong"
            else:
                color_text = "Bright"
        elif 57 <= s_mean < 142:
            if abs(v_mean - 31) < abs(v_mean - 102) and abs(v_mean - 31) < abs(v_mean - 182) and abs(v_mean - 31) < abs(v_mean - 225):
                color_text = "Dark"
            elif abs(v_mean - 102) < abs(v_mean - 31) and abs(v_mean - 102) < abs(v_mean - 182) and abs(v_mean - 102) < abs(v_mean - 225):
                color_text = "Dull"
            elif abs(v_mean - 182) < abs(v_mean - 31) and abs(v_mean - 182) < abs(v_mean - 102) and abs(v_mean - 182) < abs(v_mean - 225):
                color_text = "Soft"
            else:
                color_text = "Light"
        else:
            if abs(v_mean - 31) < abs(v_mean - 102) and abs(v_mean - 31) < abs(v_mean - 182) and abs(v_mean - 31) < abs(v_mean - 225):
                color_text = "Dark Grayish"
            elif abs(v_mean - 102) < abs(v_mean - 31) and abs(v_mean - 102) < abs(v_mean - 182) and abs(v_mean - 102) < abs(v_mean - 225):
                color_text = "Grayish"
            elif abs(v_mean - 182) < abs(v_mean - 31) and abs(v_mean - 182) < abs(v_mean - 102) and abs(v_mean - 182) < abs(v_mean - 225):
                color_text = "Light Grayish"
            else:
                color_text = "Pale"