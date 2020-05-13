'''
Created on 2019/09/06
'''

from decode.rlen import RLENGRIB2
from GPV import Meta

class Ggis1km(RLENGRIB2):
    class Section0:
        name = 0
        def __init__(self, grib, _, document_field, grib_version, bytes_length):
            self.grib = grib
            self.document_field = document_field
            self.grib_version = grib_version
            self.bytes_length = bytes_length

    class Section1:
        name = 1
        def __init__(self, length, center, secondary_center, grib_master_version, grib_local_version,
                     reference_time, document_datetime, create_status, document_type):
            self.length = length
            self.center = center
            self.secondary_center = secondary_center
            self.grib_master_version = grib_master_version
            self.grib_local_version = grib_local_version
            self.reference_time = reference_time
            self.document_datetime = document_datetime
            self.create_status = create_status
            self.document_type = document_type

    class Section3:
        name = 3
        def __init__(self, length, lattice_system, num_of_points, _a, _b, lattice_system_definition_template_num,
                     earth_shape, _c, _d,
                     long_axis_scale_factor, long_axis_scale_length, short_axis_scale_factor, short_axis_scale_length,
                     lat_points, lng_points, base_angle, _e, first_lat, first_lng, resolution_and_component_flag,
                     last_lat, last_lng, incremental_i, incremental_j, scanning_mode):
            self.length = length
            self.lattice_system = lattice_system
            self.num_of_points = num_of_points
            self.lattice_system_definition_template_num = lattice_system_definition_template_num
            self.earth_shape = earth_shape
            self.long_axis_scale_factor = long_axis_scale_factor
            self.long_axis_scale_length = long_axis_scale_length
            self.short_axis_scale_factor = short_axis_scale_factor
            self.short_axis_scale_length = short_axis_scale_length
            self.lat_points = lat_points
            self.lng_points = lng_points
            self.base_angle = base_angle
            self.first_lat = first_lat
            self.first_lng = first_lng
            self.resolution_and_component_flag = resolution_and_component_flag
            self.last_lat = last_lat
            self.last_lng = last_lng
            self.incremental_i = incremental_i
            self.incremental_j = incremental_j
            self.scanning_mode = scanning_mode

    class Section4:
        name = 4
        def __init__(self, length, _a, product_template_num, param_category, param_num, processing_type,
                     value_type, _b, _c, _d, _e, _f, first_fixed_surface_type, _g, _h, _i, _j, _k,
                     all_timedelta_finish_datetime, _l, _m, statistical_processing_type,
                     statistical_processing_unit, statistical_processing_timedelta, _n, _o, _p,
                     radar_operation_info, rf_conversion_factor_operation_info, _q):
            self.length = length
            self.product_template_num = product_template_num
            self.param_category = param_category
            self.param_num = param_num
            self.processing_type = processing_type
            self.value_type = value_type
            self.first_fixed_surface_type = first_fixed_surface_type
            self.all_timedelta_finish_datetime = all_timedelta_finish_datetime
            self.statistical_processing_type = statistical_processing_type
            self.statistical_processing_unit = statistical_processing_unit
            self.statistical_processing_timedelta = statistical_processing_timedelta
            self.radar_operation_info = radar_operation_info
            self.rf_conversion_factor_operation_info = rf_conversion_factor_operation_info

    class Section5:
        name = 5
        def __init__(self, length, num_of_all_document_points, document_template_num, num_of_bits_by_one_data,
                     use_max_level_value, max_level_value, scale_factor, i):
            self.length = length
            self.num_of_all_document_points = num_of_all_document_points
            self.document_template_num = document_template_num
            self.num_of_bits_by_one_data = num_of_bits_by_one_data
            self.use_max_level_value = use_max_level_value
            self.max_level_value = max_level_value
            self.scale_factor = scale_factor
            self.level_data_representative_value =[0]
            self.level_data_representative_value += [i(16 + 2 * nn,17 + 2 * nn) for nn in range(1, max_level_value+1)]

    class Section6:
        name = 6
        def __init__(self, length, bitmap_indicator):
            self.length = length
            self.bitmap_indicator = bitmap_indicator

    class Section7:
        name = 7
        def __init__(self, length, run_length_octet_strings):
            self.length = length
            self.run_length_octet_strings = run_length_octet_strings

    def get_nx(self):
        return self.section3.lat_points
    def get_ny(self):
        return self.section3.lng_points
    def get_baselon(self):
        return self.section3.first_lng
    def get_baselat(self):
        return self.section3.first_lat
    def get_dlon(self):
        return self.section3.incremental_i
    def get_dlat(self):
        return self.section3.incremental_j
    def get_meta(self):
        nx = self.get_nx()
        ny = self.get_ny()
        wlon = float(self.get_baselon())/1000000
        nlat = float(self.get_baselat())/1000000
        dlon = float(self.get_dlon())/1000000
        dlat = float(self.get_dlat())/1000000
        meta = Meta(nx=nx, ny=ny, wlon=wlon, nlat=nlat, dlon=dlon, dlat=dlat)
        return meta

    def read(self):
        b  = self.r
        i  = self.r_int
        s  = self.r_str
        dt = self.r_dt

        # 第 0 節
        self.section0 = Ggis1km.Section0(s(1,4), i(5,6), i(7), i(8), i(9, 16))
        # 第 1 節
        sec_length = i(1,4)
        sec_name = i(5)
        if sec_name == 1:
            self.section1 = Ggis1km.Section1(sec_length, i(6,7), i(8,9), i(10), i(11), i(12), dt(13), i(20), i(21))
        # 第 3 節
        sec_length = i(1,4)
        sec_name = i(5)
        if sec_name == 3:
            self.section3 = Ggis1km.Section3(sec_length, i(6), i(7, 10), i(11), i(12), i(13,14), i(15), i(16),
                                             i(17, 20), i(21),i(22, 25), i(26), *[i(27, 30) for _ in range(7)],
                                             i(55), i(56, 59), i(60, 63),i(64, 67),i(68, 71), i(72))
        # 第 4 節
        sec_length = i(1,4)
        sec_name = i(5)
        if sec_name == 4:
            self.section4 = Ggis1km.Section4(sec_length, i(6,7), i(8,9), *[i(10) for _ in range(10, 15)],
                                             i(15,16), i(17), i(18), i(19,22), i(23), i(24), i(25,28), i(29), i(30),
                                             i(31,34), dt(35), i(42), i(43,46), i(47), i(48), i(49), i(50,53), i(54),
                                             i(55,58), i(59,66), i(67,74), i(75,82))
        # 第 5 節
        sec_length = i(1,4)
        sec_name = i(5)
        if sec_name == 5:
            self.section5 = Ggis1km.Section5(sec_length, i(6,9), i(10,11), i(12), i(13,14), i(15,16), i(17),i)
        # 第 6 節
        sec_length = i(1,4)
        sec_name = i(5)
        if sec_name == 6:
            self.section6 = Ggis1km.Section6(sec_length, i(6))
        # 第 7 節
        sec_length = i(1,4)
        sec_name = i(5)
        if sec_name == 7:
            self.section7 = Ggis1km.Section7(sec_length, b(6,sec_length))
        #self.leveldata = self.decode_rle(self.section7.run_length_octet_strings, 8, self.section5.use_max_level_value)
        self.data = self.decode_rle_to_float(
                                self.section7.run_length_octet_strings,
                                8,
                                self.section5.use_max_level_value,
                                leveltable=self.section5.level_data_representative_value)
        flag = s(1,4)
        if flag == '7777':
            return