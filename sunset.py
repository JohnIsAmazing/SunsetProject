def main():
    # there is no error handling in this code.
    # if you put something stupid in, it will crash
    # python 3.7.1

    s = sunset()

    #C0 - C2
    # For cloud coverage:
    #   O=overcast, B=broken, A=scattered, C=clear or unknown
    print('something stupid') #scott is adding something studpid to crash the program
    s.clouds_horizon_high  = 'C'
    s.clouds_overhead_high = 'C'
    s.cloud_high_vertical_development = False

    s.clouds_horizon_med   = 'A'
    s.clouds_overhead_med  = 'A'
    s.cloud_med_vertical_development = False

    s.clouds_horizon_low   = 'C'
    s.clouds_overhead_low  = 'C'
    s.cloud_low_vertical_development = False

    # C3
    s.horizon_visible = True
    s.green_flash = False
    s.haze_or_smoke = False
    s.contrails = False
    s.oat = 60 # Outside Air Temperature in °F
    s.wind = 'lots' # possible values 'none','calm','lots'

    #C4
    s.overall_visibility = 5 # possible values 0,1,2,3,4
    s.virga = False
    s.visible_rain = False
    s.local_rain = False

    #C5
    s.stripes_on_sum = False
    s.sun_rays_down = False
    s.sun_rays_up = False
    s.horizon_clouds_top_stripe = False
    s.sun_distorted = False

    #C6, Faircove only
    s.unusual_island_shapes = False
    s.malibu_reflections = False
    s.multi_color_ocean = False
    s.low_clouds_were_above = False

    #C7, Faircove only
    s.see_point_dume = True
    s.see_anacapa = True
    s.see_sb_island = True
    s.see_san_nic_island = True
    s.see_malibu = True

    print(s.sunset_code_faircove)
    #print(s.sunset_code_generic)
    #print(s.sunset_code_hexish)
    #print(s.sunset_code_binary)
    print(s.decode)

    print('')

    s_michele = sunset()
    s_michele.sunset_code_hexish = 'MICHELEJ'
    print(s_michele.sunset_code_faircove)
    print(s_michele.decode)


class sunset:
    """ Generates a code for your observed sunset OR generate a sunset description from your code. """

    # 2019-01-01 Version 1.00
    #
    # 2019-01-05 Version 1.01
    #   Changed cloud coverage algorithm to result in hexish code 'CLS' for clear skys.
    #
    # 2019-01-12 Version 1.02
    #   Create two properties, sunset_code_hexish and sunset_code_binary.
    #   sunset_code_hexish is now used in sunset_code property to avoid duplicate code
    #
    #   Moved the green flash parameter from a special variable to hex char[3] postion [2] and
    #   redid output properties to match.
    #
    #   Split the code output to sunset_code_faircove and sunset_code_generic
    #
    # 2019-02-18 Version 1.03
    #   Add input parameters for wind and temperature that are used to calculate comfort zone.
    #   Add ability to set sunset_code_hexish
    #   Add preliminary parameter sunset.decode
    #
    # 2019-02-19 Version 1.04
    #   Fixed green flash in decode text.


    # Task List
    #
    # 1. Create a decoder, code to text.

    def __init__(self):
        self.code_chars = []
        self.__oat = 0
        self.__wind = 'calm'
        for i in range(0,8):
            self.code_chars.append(self.HexPlus('00000'))

    # C0 - C2 cloud coverage group
    #
    @property
    def cloud_high_vertical_development(self): return self.code_chars[0].binary_list[0]
    @cloud_high_vertical_development.setter
    def cloud_high_vertical_development(self, value): self.code_chars[0].binary_list_insert(value=str(int(value)),position=0)

    @property
    def clouds_horizon_high(self): return self.code_chars[0].binary_list[1] + self.code_chars[0].binary_list[2]
    @clouds_horizon_high.setter
    def clouds_horizon_high(self, value):
        if value == 'O':
            self.code_chars[0].binary_list_insert(value='0',position=1)
            self.code_chars[0].binary_list_insert(value='0',position=2)
        elif value == 'B':
            self.code_chars[0].binary_list_insert(value='0',position=1)
            self.code_chars[0].binary_list_insert(value='1',position=2)
        elif value == 'A':
            self.code_chars[0].binary_list_insert(value='1',position=1)
            self.code_chars[0].binary_list_insert(value='0',position=2)
        elif value == 'C':
            self.code_chars[0].binary_list_insert(value='1',position=1)
            self.code_chars[0].binary_list_insert(value='1',position=2)

    @property
    def clouds_overhead_high(self): return self.code_chars[0].binary_list[3] + self.code_chars[0].binary_list[4]
    @clouds_overhead_high.setter
    def clouds_overhead_high(self, value):
        if value == 'C':
            self.code_chars[0].binary_list_insert(value='0',position=3)
            self.code_chars[0].binary_list_insert(value='0',position=4)
        elif value == 'A':
            self.code_chars[0].binary_list_insert(value='0',position=3)
            self.code_chars[0].binary_list_insert(value='1',position=4)
        elif value == 'B':
            self.code_chars[0].binary_list_insert(value='1',position=3)
            self.code_chars[0].binary_list_insert(value='0',position=4)
        elif value == 'O':
            self.code_chars[0].binary_list_insert(value='1',position=3)
            self.code_chars[0].binary_list_insert(value='1',position=4)

    @property
    def cloud_med_vertical_development(self): return self.code_chars[1].binary_list[0]
    @cloud_med_vertical_development.setter
    def cloud_med_vertical_development(self, value):
        if value:
            self.code_chars[1].binary_list_insert(value='0')
        else:
            self.code_chars[1].binary_list_insert(value='1')

    @property
    def clouds_horizon_med(self): return self.code_chars[1].binary_list[1] + self.code_chars[1].binary_list[2]
    @clouds_horizon_med.setter
    def clouds_horizon_med(self, value):
        if value == 'A':
            self.code_chars[1].binary_list_insert(value='0',position=1)
            self.code_chars[1].binary_list_insert(value='0',position=2)
        elif value == 'C':
            self.code_chars[1].binary_list_insert(value='0',position=1)
            self.code_chars[1].binary_list_insert(value='1',position=2)
        elif value == 'O':
            self.code_chars[1].binary_list_insert(value='1',position=1)
            self.code_chars[1].binary_list_insert(value='0',position=2)
        elif value == 'B':
            self.code_chars[1].binary_list_insert(value='1',position=1)
            self.code_chars[1].binary_list_insert(value='1',position=2)

    @property
    def clouds_overhead_med(self): return self.code_chars[1].binary_list[3] + self.code_chars[1].binary_list[4]
    @clouds_overhead_med.setter
    def clouds_overhead_med(self, value):
        if value == 'O':
            self.code_chars[1].binary_list_insert(value='0',position=3)
            self.code_chars[1].binary_list_insert(value='0',position=4)
        elif value == 'C':
            self.code_chars[1].binary_list_insert(value='0',position=3)
            self.code_chars[1].binary_list_insert(value='1',position=4)
        elif value == 'B':
            self.code_chars[1].binary_list_insert(value='1',position=3)
            self.code_chars[1].binary_list_insert(value='0',position=4)
        elif value == 'A':
            self.code_chars[1].binary_list_insert(value='1',position=3)
            self.code_chars[1].binary_list_insert(value='1',position=4)

    @property
    def cloud_low_vertical_development(self): return self.code_chars[2].binary_list[0]
    @cloud_low_vertical_development.setter
    def cloud_low_vertical_development(self, value):
        if value:
            self.code_chars[2].binary_list_insert(value='0')
        else:
            self.code_chars[2].binary_list_insert(value='1')

    @property
    def clouds_horizon_low(self): return self.code_chars[2].binary_list[1] + self.code_chars[2].binary_list[2]
    @clouds_horizon_low.setter
    def clouds_horizon_low(self, value):
        if value == 'A':
            self.code_chars[2].binary_list_insert(value='0',position=1)
            self.code_chars[2].binary_list_insert(value='0',position=2)
        elif value == 'B':
            self.code_chars[2].binary_list_insert(value='0',position=1)
            self.code_chars[2].binary_list_insert(value='1',position=2)
        elif value == 'O':
            self.code_chars[2].binary_list_insert(value='1',position=1)
            self.code_chars[2].binary_list_insert(value='0',position=2)
        elif value == 'C':
            self.code_chars[2].binary_list_insert(value='1',position=1)
            self.code_chars[2].binary_list_insert(value='1',position=2)

    @property
    def clouds_overhead_low(self): return self.code_chars[2].binary_list[3] + self.code_chars[2].binary_list[4]
    @clouds_overhead_low.setter
    def clouds_overhead_low(self, value):
        if value == 'B':
            self.code_chars[2].binary_list_insert(value='0',position=3)
            self.code_chars[2].binary_list_insert(value='0',position=4)
        elif value == 'A':
            self.code_chars[2].binary_list_insert(value='0',position=3)
            self.code_chars[2].binary_list_insert(value='1',position=4)
        elif value == 'O':
            self.code_chars[2].binary_list_insert(value='1',position=3)
            self.code_chars[2].binary_list_insert(value='0',position=4)
        elif value == 'C':
            self.code_chars[2].binary_list_insert(value='1',position=3)
            self.code_chars[2].binary_list_insert(value='1',position=4)

    # C3 sky conditions group
    #
    @property
    def oat(self): return self.__oat
    @oat.setter
    def oat(self, value):
        self.__oat = value
        self.set_comfort_zone(self.__wind,self.__oat)

    @property
    def wind(self): return self.__wind
    @wind.setter
    def wind(self, value):
        self.__wind = value
        self.set_comfort_zone(self.__wind,self.__oat)

    @property
    def comfort_zone(self): return self.code_chars[3].binary_list[0]
    #@comfort_zone.setter
    def set_comfort_zone(self, obsv_wind, obsv_oat):
        cz = False
        if obsv_wind == 'none' and obsv_oat > 70 and obsv_oat < 81: cz = True
        if obsv_wind == 'calm' and obsv_oat > 74 and obsv_oat < 86: cz = True
        self.code_chars[3].binary_list_insert(value=str(int(cz)),position=0)

    @property
    def horizon_visible(self): return self.code_chars[3].binary_list[1]
    @horizon_visible.setter
    def horizon_visible(self, value): self.code_chars[3].binary_list_insert(value=str(int(value)),position=1)

    @property
    def green_flash(self):
        if self.code_chars[3].binary_list[2] == '0': return False
        else: return True
        #return self.code_chars[3].binary_list[2]
    @green_flash.setter
    def green_flash(self, value):
        self.code_chars[3].binary_list_insert(value=str(int(value)),position=2)
        print (self.green_flash)

    @property
    def haze_or_smoke(self): return self.code_chars[3].binary_list[2]
    @haze_or_smoke.setter
    def haze_or_smoke(self, value): self.code_chars[3].binary_list_insert(value=str(int(value)),position=3)

    @property
    def contrails(self): return self.code_chars[3].binary_list[2]
    @contrails.setter
    def contrails(self, value): self.code_chars[3].binary_list_insert(value=str(int(value)),position=4)

    # C4 visbility and weather
    #
    @property
    def virga(self): return self.code_chars[4].binary_list[0]
    @virga.setter
    def virga(self, value): self.code_chars[4].binary_list_insert(value=str(int(value)),position=0)

    @property
    def overall_visibility(self): return self.code_chars[4].binary_list[1] + self.code_chars[4].binary_list[2]
    @overall_visibility.setter
    def overall_visibility(self, value):
        if   value <= 1:
            self.code_chars[4].binary_list_insert(value='0',position=1)
            self.code_chars[4].binary_list_insert(value='0',position=2)
        elif value == 2:
            self.code_chars[4].binary_list_insert(value='0',position=1)
            self.code_chars[4].binary_list_insert(value='1',position=2)
        elif value == 3:
            self.code_chars[4].binary_list_insert(value='1',position=1)
            self.code_chars[4].binary_list_insert(value='0',position=2)
        elif value >= 4:
            self.code_chars[4].binary_list_insert(value='1',position=1)
            self.code_chars[4].binary_list_insert(value='1',position=2)

    @property
    def visible_rain(self): return self.code_chars[4].binary_list[3]
    @visible_rain.setter
    def visible_rain(self, value): self.code_chars[4].binary_list_insert(value=str(int(value)),position=3)

    @property
    def local_rain(self): return self.code_chars[4].binary_list[4]
    @local_rain.setter
    def local_rain(self, value): self.code_chars[4].binary_list_insert(value=str(int(value)),position=4)

    # C5 Visual Distortions
    #
    @property
    def sun_distorted(self): return self.code_chars[5].binary_list[0]
    @sun_distorted.setter
    def sun_distorted(self, value): self.code_chars[5].binary_list_insert(value=str(int(value)),position=0)

    @property
    def stripes_on_sun(self): return self.code_chars[5].binary_list[1]
    @stripes_on_sun.setter
    def stripes_on_sun(self, value): self.code_chars[5].binary_list_insert(value=str(int(value)),position=1)

    @property
    def sun_rays_down(self): return self.code_chars[5].binary_list[2]
    @sun_rays_down.setter
    def sun_rays_down(self, value): self.code_chars[5].binary_list_insert(value=str(int(value)),position=2)

    @property
    def sun_rays_up(self): return self.code_chars[5].binary_list[3]
    @sun_rays_up.setter
    def sun_rays_up(self, value): self.code_chars[5].binary_list_insert(value=str(int(value)),position=3)

    @property
    def horizon_clouds_top_stripe(self): return self.code_chars[5].binary_list[4]
    @horizon_clouds_top_stripe.setter
    def horizon_clouds_top_stripe(self, value): self.code_chars[5].binary_list_insert(value=str(int(value)),position=4)

    # C6 Faircove specific
    #

    @property
    def unusual_island_shapes(self): return self.code_chars[6].binary_list[0]
    @unusual_island_shapes.setter
    def unusual_island_shapes(self, value): self.code_chars[6].binary_list_insert(value=str(int(value)),position=0)

    @property
    def low_clouds_were_above(self): return self.code_chars[6].binary_list[1]
    @low_clouds_were_above.setter
    def low_clouds_were_above(self, value): self.code_chars[6].binary_list_insert(value=str(int(value)),position=1)

    @property
    def malibu_reflections(self): return self.code_chars[6].binary_list[2]
    @malibu_reflections.setter
    def malibu_reflections(self, value): self.code_chars[6].binary_list_insert(value=str(int(value)),position=2)

    @property
    def multi_color_ocean(self): return self.code_chars[6].binary_list[4]
    @multi_color_ocean.setter
    def multi_color_ocean(self, value): self.code_chars[6].binary_list_insert(value=str(int(value)),position=4)

    # C7 Faircove specific
    #
    @property
    def see_malibu(self): return self.code_chars[7].binary_list[0]
    @see_malibu.setter
    def see_malibu(self, value): self.code_chars[7].binary_list_insert(value=str(int(value)),position=0)

    @property
    def see_point_dume(self): return self.code_chars[7].binary_list[1]
    @see_point_dume.setter
    def see_point_dume(self, value): self.code_chars[7].binary_list_insert(value=str(int(value)),position=1)

    @property
    def see_anacapa(self): return self.code_chars[7].binary_list[2]
    @see_anacapa.setter
    def see_anacapa(self, value): self.code_chars[7].binary_list_insert(value=str(int(value)),position=2)

    @property
    def see_sb_island(self): return self.code_chars[7].binary_list[3]
    @see_sb_island.setter
    def see_sb_island(self, value): self.code_chars[7].binary_list_insert(value=str(int(value)),position=3)

    @property
    def see_san_nic_island(self): return self.code_chars[7].binary_list[4]
    @see_san_nic_island.setter
    def see_san_nic_island(self, value): self.code_chars[7].binary_list_insert(value=str(int(value)),position=4)

    # sunset code output
    #
    @property
    def sunset_code_faircove(self):
        code_string = 'J&K Sunset Code V1.03(F): ' + self.sunset_code_hexish[:6] + r'/' +  self.sunset_code_hexish[6:8]
        if self.green_flash:
            code_string += '-GF'
        return code_string

    @property
    def sunset_code_generic(self):
        code_string = 'J&K Sunset Code V1.03(G): ' + self.sunset_code_hexish[:6]
        if self.green_flash:
            code_string += '-GF'

        return code_string

    @property
    def sunset_code_hexish(self):
        code_h = ''
        for c in self.code_chars:
            code_h += c.hexish
        return code_h
    @sunset_code_hexish.setter
    def sunset_code_hexish(self, value):
        #value does not include '-GF' i.e. 'CLS456AB'
        bs = ''
        pos = 0
        self.code_chars.clear()
        for c in value:
            b = self.HexPlus(c)
            self.code_chars.append(b)
            #bs += c.binary_string

    @property
    def sunset_code_binary(self):
        code_b = ''
        for c in self.code_chars:
            code_b += c.binary_string + ' '
        return code_b

    @property
    def decode(self):
        # decodes a sunset code into plain text
        #
        decode_text = 'Sunset Description:\n'
        decode_text += 'The weather was pleasant. ' if self.comfort_zone == '1' else 'The weather was less than perfect. '
        decode_text += 'The horizon was visible. ' if self.horizon_visible == '1' else 'The horizon was obscured by clouds and/or haze. '
        decode_text += self.cloud_description
        if (self.cloud_high_vertical_development == '1'
            or self.cloud_med_vertical_development == '0'
            or self.cloud_low_vertical_development == '0'): decode_text += 'Some of the clouds had vertical development. '
        if   self.overall_visibility == '00': decode_text += 'The visibilty was terrible. '
        elif self.overall_visibility == '01': decode_text += 'The visibilty was poor. '
        elif self.overall_visibility == '10': decode_text += 'The visibilty was good but not great. '
        elif self.overall_visibility == '11': decode_text += 'The visibilty was excellent. '
        decode_text += 'There was a GREEN FLASH!! ' if self.green_flash == True else ''
        decode_text += 'There was haze and smoke causing the sky to take on an orange color. ' if self.haze_or_smoke == '1' else ''
        decode_text += 'There were contrails from jet aircraft visible. ' if self.contrails == '1' else 'No aircraft contrails were visible. '
        decode_text += 'There was virga visible. ' if self.virga == '1' else ''
        decode_text += 'Rain was visible in the distance. ' if self.visible_rain == '1' else ''
        decode_text += 'It was raining.' if self.local_rain == '1' else ''
        decode_text += 'Distortions such as sun dogs were visible just as the sun went down. ' if self.sun_distorted == '1' else ''
        decode_text += 'There were stripes visible on the sun’s disk before it set. ' if self.stripes_on_sun == '1' else ''
        decode_text += 'There were rays from the sun going down observed. ' if self.sun_rays_down == '1' else ''
        decode_text += 'There were rays from the sun going up observed. ' if self.sun_rays_up == '1' else ''
        decode_text += 'Cloud tops on the horizon were lit up from behind by the sun causing a bright outline. ' if self.horizon_clouds_top_stripe == '1' else ''
        decode_text += 'There were low clouds below us and we could see above them. ' if self.low_clouds_were_above == '1' else ''
        decode_text += 'The shapes of visible islands were distorted by atmospheric conditions. ' if self.unusual_island_shapes == '1' else ''
        decode_text += 'Orange light reflections off windows in Malibu were observed. ' if self.malibu_reflections == '1' else ''
        decode_text += 'The ocean appeared multi-colored. ' if self.multi_color_ocean == '1' else ''
        decode_text += 'Malibu was visible. ' if self.see_malibu == '1' else ''
        decode_text += 'Point Dume was visible. ' if self.see_point_dume == '1' else ''
        decode_text += 'Anacapa and Santa Cruz Islands were visible. ' if self.see_anacapa == '1' else ''
        decode_text += 'Santa Barbara Island was visible. ' if self.see_sb_island == '1' else ''
        decode_text += 'San Nicolas Island was visible behind Santa Barbara island. ' if self.see_san_nic_island == '1' else ''


        return decode_text

    @property
    def cloud_description(self):
        # helper function for decode function. Gets cloud type descriptions.
        #
        descr = ''
        if (self.clouds_horizon_high +
            self.clouds_overhead_high +
            self.clouds_horizon_med +
            self.clouds_overhead_med +
            self.clouds_horizon_low +
            self.clouds_overhead_low) == '110001011111': return 'The sky was clear of clouds. '

        if   self.clouds_horizon_high == '00': descr += 'There was a solid ceiling of high clouds on the horizon. '
        elif self.clouds_horizon_high == '01': descr += 'There were broken high clouds on the horizon. '
        elif self.clouds_horizon_high == '10': descr += 'There were scattered high clouds on the horizon. '

        if   self.clouds_overhead_high == '01': descr += 'There were high scattered clouds overhead. '
        elif self.clouds_overhead_high == '10': descr += 'There was a broken layer of high clouds overhead. '
        elif self.clouds_overhead_high == '11': descr += 'There was a solid ceiling of high clouds overhead. '

        if   self.clouds_horizon_med == '00': descr += 'There were scattered medium height clouds on the horizon. '
        elif self.clouds_horizon_med == '10': descr += 'There was a solid ceiling of medium height clouds on the horizon. '
        elif self.clouds_horizon_med == '11': descr += 'There was a broken layer of medium height clouds on the horizon. '

        if   self.clouds_overhead_med == '00': descr += 'There was a solid ceiling of medium height clouds overhead. '
        elif self.clouds_overhead_med == '10': descr += 'There was a broken layer of medium height clouds overhead. '
        elif self.clouds_overhead_med == '11': descr += 'There were medium height scattered clouds overhead. '

        if   self.clouds_horizon_low == '00': descr += 'There were scattered low clouds on the horizon. '
        elif self.clouds_horizon_low == '01': descr += 'There was a broken layer of low clouds on the horizon. '
        elif self.clouds_horizon_low == '10': descr += 'There was a solid ceiling of low clouds on the horizon. '

        if   self.clouds_overhead_low == '00': descr += 'There was a low broken cloud layer overhead. '
        elif self.clouds_overhead_low == '01': descr += 'There were low scattered clouds overhead. '
        elif self.clouds_overhead_low == '10': descr += 'There was a solid ceiling of low clouds overhead. '

        return descr


    class HexPlus:
        # Creates and maintains a "hexish" character based on four binary bits '0000' plus an
        # extra bit. The four bits define the range 0 - F. The extra bit, if = '1' bumps the character
        # up one letter in the alphabet creating a hexish character. For example 10000 is 0(hex) bumped
        # up to G(hexish) and 11101 is D(hex) bumped up to U(hexish). O (oh) is skipped because it
        # looks too much like zero so the last hexish character is W, not V. This makes for more interesting
        # sunset codes.

        def __init__(self, value = '00000'):
            self.__binary_string = ''
            if isinstance(value, str) and len(value) == 1: # its a hexish char
                self.__binary_string = self.hexish2bin(value)
            elif isinstance(value, str) and len(value) == 5: # its a binary
                self.__binary_string = value
            elif isinstance(value, list) and len(value) == 5: # its a binary list
                for p in value:
                    self.__binary_string += p
            else: # its an error
                self.__binary_string = 'error'

        @property
        def binary_string(self):
            return self.__binary_string
        @binary_string.setter
        def binary_string(self, value):
            self.__binary_string = value

        @property
        def binary_list(self):
            return_list = []
            for p in self.__binary_string:
                return_list.append(p)
            return return_list
        @binary_list.setter
        def binary_list(self, value):
            self.__binary_string = ''
            for p in value:
                self.__binary_string += p

        @property
        def hexish(self):
            return self.bin2hexish(self.__binary_string)
        @hexish.setter
        def hexish(self, value):
            self.__binary_string = self.hexish2bin(value)

        def binary_list_insert(self, value='1', position=0):
            bl = self.binary_list
            bl[position] = value
            self.__binary_string = ''
            for b in bl:
                self.__binary_string += b

        def bin2hexish(self, bin_value):
            if   bin_value == '00000': return '0'
            elif bin_value == '00001': return '1'
            elif bin_value == '00010': return '2'
            elif bin_value == '00011': return '3'
            elif bin_value == '00100': return '4'
            elif bin_value == '00101': return '5'
            elif bin_value == '00110': return '6'
            elif bin_value == '00111': return '7'
            elif bin_value == '01000': return '8'
            elif bin_value == '01001': return '9'
            elif bin_value == '01010': return 'A'
            elif bin_value == '01011': return 'B'
            elif bin_value == '01100': return 'C'
            elif bin_value == '01101': return 'D'
            elif bin_value == '01110': return 'E'
            elif bin_value == '01111': return 'F'
            elif bin_value == '10000': return 'G'
            elif bin_value == '10001': return 'H'
            elif bin_value == '10010': return 'I'
            elif bin_value == '10011': return 'J'
            elif bin_value == '10100': return 'K'
            elif bin_value == '10101': return 'L'
            elif bin_value == '10110': return 'M'
            elif bin_value == '10111': return 'N'
            elif bin_value == '11000': return 'P'
            elif bin_value == '11001': return 'Q'
            elif bin_value == '11010': return 'R'
            elif bin_value == '11011': return 'S'
            elif bin_value == '11100': return 'T'
            elif bin_value == '11101': return 'U'
            elif bin_value == '11110': return 'V'
            elif bin_value == '11111': return 'W'
            else: return 'Z'

        def hexish2bin(self, hexish_value):
            if   hexish_value == '0': return '00000'
            elif hexish_value == '1': return '00001'
            elif hexish_value == '2': return '00010'
            elif hexish_value == '3': return '00011'
            elif hexish_value == '4': return '00100'
            elif hexish_value == '5': return '00101'
            elif hexish_value == '6': return '00110'
            elif hexish_value == '7': return '00111'
            elif hexish_value == '8': return '01000'
            elif hexish_value == '9': return '01001'
            elif hexish_value == 'A': return '01010'
            elif hexish_value == 'B': return '01011'
            elif hexish_value == 'C': return '01100'
            elif hexish_value == 'D': return '01101'
            elif hexish_value == 'E': return '01110'
            elif hexish_value == 'F': return '01111'
            elif hexish_value == 'G': return '10000'
            elif hexish_value == 'H': return '10001'
            elif hexish_value == 'I': return '10010'
            elif hexish_value == 'J': return '10011'
            elif hexish_value == 'K': return '10100'
            elif hexish_value == 'L': return '10101'
            elif hexish_value == 'M': return '10110'
            elif hexish_value == 'N': return '10111'
            elif hexish_value == 'P': return '11000'
            elif hexish_value == 'Q': return '11001'
            elif hexish_value == 'R': return '11010'
            elif hexish_value == 'S': return '11011'
            elif hexish_value == 'T': return '11100'
            elif hexish_value == 'U': return '11101'
            elif hexish_value == 'V': return '11110'
            elif hexish_value == 'W': return '11111'
            else: return 'error'

if __name__ == '__main__':
    main()
