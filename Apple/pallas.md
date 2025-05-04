# Pallas
Pallas is a authoritative server component to mobileassetd that runs on all internet-connected Apple devices. (Note that mobileassetd does not run things like the AirTag or other accessories, but could potentially run on a device like the Studio Display based on WatchOS functionality for updating assets.)

## Asset Types
Also known as Asset Specifiers (RE: Xcode's Bundle Indentifiers), this explicitly defines separate assets that can be updated via the mobileasset/pallas request pattern. Pallas is authoritative, and mobileasset is beholden to whatever Pallas returns.

It's worth noting that I have not tried to overwrite any responses returned by Pallas and I would not expect anything to be guaranteed here (but SUs have a process that prevents spoofing the response, not sure about other processes or daemons on the device).

### UnifiedAssetFramework (UAF)
One of the more common asset types is the [Unified Asset Framework (UAF)](https://theapplewiki.com/wiki/UnifiedAssetFramework). Per the AppleWiki, "Not much is known about UnifiedAssetFramework other than its abbreviation 'UAF' and that it relates to Siri and Apple Intelligence models or features."

## Servers
Easiest TLDR ever;
- (current) https://gdmf.apple.com/v2/assets
- (old) https://mesu.apple.com

### MESU
Mesu was an original asset server that hosted XML files before REST requests were possible. With a few changes and some APIs that became more common, instead of needing a bigger CDN to handle requests, servers that could dynamically update and manage content via APIs took over. Something something, I'm rambling, so don't mind me.

Example (source: [applewiki](https://theapplewiki.com/wiki/MobileAsset#Mesu)): [`https://mesu.apple.com/assets/macos/com_apple_MobileAsset_TimeZoneUpdates/com_apple_MobileAsset_TimeZoneUpdate.xml`](https://mesu.apple.com/assets/macos/com_apple_MobileAsset_TimeZoneUpdates/com_apple_MobileAsset_TimeZoneUpdate.xml)

## Some Links/References
- [Pallas.py](https://github.com/riigess/pallas.py), an exploritory repo that dives deeper into making requests to Pallas
- [The Apple Wiki page on MobileAsset](https://theapplewiki.com/wiki/MobileAsset)