import math

pixel_size_m = 0.38  # meters per pixel
bearing_degrees = 335  # drone heading
image_center_x = 320
image_center_y = 256
checkpoint_x = 558
checkpoint_y = 328

checkpoint_lat = 50.603694
checkpoint_lon = 30.650625

dx_pixels = checkpoint_x - image_center_x
dy_pixels = checkpoint_y - image_center_y

dx_m = dx_pixels * pixel_size_m
dy_m = dy_pixels * pixel_size_m

bearing_rad = math.radians(bearing_degrees)

north_offset = dx_m * math.sin(bearing_rad) + dy_m * math.cos(bearing_rad)
east_offset = dx_m * math.cos(bearing_rad) - dy_m * math.sin(bearing_rad)

meters_per_deg_lat = 111_320
meters_per_deg_lon = 40075000 * math.cos(math.radians(checkpoint_lat)) / 360

dlat = -north_offset / meters_per_deg_lat
dlon = -east_offset / meters_per_deg_lon

image_center_lat = checkpoint_lat + dlat
image_center_lon = checkpoint_lon + dlon

print("Estimated center of image:")
print("Latitude:", image_center_lat)
print("Longitude:", image_center_lon)

