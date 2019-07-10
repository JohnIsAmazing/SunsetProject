from sunset import sunset

def main():
    # there is no error handling in this code.
    # if you put something stupid in, it will crash
    # python 3.7.1

    s = sunset()

    #C0 - C2
    # For cloud coverage:
    #   O=overcast, B=broken, A=scattered, C=clear or unknown
    s.clouds_horizon_high  = 'O' 
    s.clouds_overhead_high = 'A'
    s.cloud_high_vertical_development = False

    s.clouds_horizon_med   = 'C'
    s.clouds_overhead_med  = 'A'
    s.cloud_med_vertical_development = True

    s.clouds_horizon_low   = 'C'
    s.clouds_overhead_low  = 'C'
    s.cloud_low_vertical_development = False

    # C3
    s.horizon_visible = False
    s.green_flash = False
    s.haze_or_smoke = False
    s.contrails = True
    #s.comfort_zone = False
    s.oat = 60 # Outside Air Temperature in °F
    s.wind = 'calm' # possible values none,calm,lots
    
    #C4
    s.overall_visibility = 2 # possible values 0,1,2,3,4
    s.virga = True
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
    s.see_point_dume = False
    s.see_anacapa = False
    s.see_sb_island = False
    s.see_san_nic_island = False
    s.see_malibu = False

    print(s.sunset_code_faircove)
    print(s.sunset_code_generic)
    #print(s.sunset_code_hexish)
    print(s.sunset_code_binary)
    print(s.decode)
    #print(s.cloud_high_vertical_development)
    #print(s.cloud_med_vertical_development)
    #print(s.cloud_low_vertical_development)

    #ss = sunset()
    #ss.sunset_code_hexish = 'DSSLVJLS'
    #ss.sunset_code_hexish = 'JENNIFER'
    #print('')
    #print(ss.sunset_code_faircove)
    #print(ss.decode)
    #print(s.sunset_code_binary)
    #print(ss.cloud_med_vertical_development)
    #print(ss.sunset_code_faircove)


if __name__ == '__main__':
    main()
