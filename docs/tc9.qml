<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="2.18.14" minimumScale="inf" maximumScale="1e+08" hasScaleBasedVisibilityFlag="0">
  <pipe>
    <rasterrenderer opacity="1" alphaBand="-1" classificationMax="89.92" classificationMinMaxOrigin="CumulativeCutFullExtentEstimated" band="1" classificationMin="20" type="singlebandpseudocolor">
      <rasterTransparency/>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" clip="0">
          <item alpha="255" value="10" label="Planar-planar" color="#ffff00"/>
          <item alpha="255" value="20" label="Convex-planar" color="#00ff00"/>
          <item alpha="255" value="30" label="Concave-planar" color="#00ff80"/>
          <item alpha="255" value="40" label="Planar-convex" color="#00ffff"/>
          <item alpha="255" value="50" label="Convex-convex" color="#0080ff"/>
          <item alpha="255" value="60" label="Concave-convex" color="#0000ff"/>
          <item alpha="255" value="70" label="Planar-concave" color="#8000ff"/>
          <item alpha="255" value="80" label="Convex-concave" color="#ff00ff"/>
          <item alpha="255" value="90" label="Concave-concave" color="#ff0000"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" contrast="0"/>
    <huesaturation colorizeGreen="128" colorizeOn="0" colorizeRed="255" colorizeBlue="128" grayscaleMode="0" saturation="0" colorizeStrength="100"/>
    <rasterresampler maxOversampling="2"/>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
