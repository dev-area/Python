import roonapi as rn
appinfo = {
        "extension_id": "python_roon_test",
        "display_name": "Python library for Roon",
        "display_version": "1.0.0",
        "publisher": "marcelveldt",
        "email": "mygreat@emailaddress.com"
    }
f = open('tk','r')
t = f.read(50)
t
rapi = rn.RoonApi(appinfo,token=t)
rapi.mute()
help(rapi)
rapi.outputs
rapi.mute(output_id='1701b216880570dfdbda9b4efcf33cf617ad')
rapi.mute(output_id='1701b216880570dfdbda9b4efcf33cf617ad',mute=False)
help(rapi.playback_control)
help(rapi.playback_control)
rapi.playback_control(control='next')
rapi.playback_control(zone_or_output_id='1701b216880570dfdbda9b4efcf33cf617ad' control='next')
rapi.playback_control(zone_or_output_id='1701b216880570dfdbda9b4efcf33cf617ad', control='next')
rapi.playback_control(zone_or_output_id='1701b216880570dfdbda9b4efcf33cf617ad', control='next')
rapi.get_image()
help(rapi.get_image)
import roonapi.roonapi as rp
rp.ServiceStatus()
rp.ServiceStatus
rp.ServiceBrowse
rapi.browse_browse()
help(rapi)
rapi.__dict__
rn.discovery
import roonapi.discovery as rd
rd.RoonDiscovery()
rapi.zones
type(rapi.zones)
rapi.get_image('23a33da5e2a3e38428afbf97ca341c7f')
