from server_parts.models import Server as Serv, ObjsInfo, Obj35mMeTe, Obj31mDpTb, Obj30mSpTb, Obj58cScTa, Obj59cDcTa
from devs.models import Device
from cards.models import Card
from support_functions import ioa_to_address, update_address
import pou


class Server:
    def __init__(self, name, server_iteration):
        self.name = name
        self.server_iteration = server_iteration
        self.header = Serv.objects.first().Header
        self.closing_tag = Serv.objects.first().ClosingTag

    def headers(self, file):
        header = self.header.format(self.name, str(self.server_iteration), str(2404 + self.server_iteration),
                                    str(self.server_iteration))
        file.write(header)

    def closing_tags(self, file):
        file.write(self.closing_tag)


class ServerDevice:
    def __init__(self, name, server_iteration):
        self.name = name
        self.server_iteration = server_iteration
        self.monitor_ioa = Device.objects.filter(Name=name).first().MonitorIoa
        self.monitor_ioa_jump = Device.objects.filter(Name=name).first().MonitorIoaJump
        self.monitor_obj_list = Device.objects.filter(Name=name).first().MonitorObjectList.split(",")
        self.monitor_obj_list = [i.strip() for i in self.monitor_obj_list]
        self.control_ioa = Device.objects.filter(Name=name).first().ControlIoa
        self.control_ioa_jump = Device.objects.filter(Name=name).first().ControlIoaJump
        self.control_obj_list = Device.objects.filter(Name=name).first().ControlObjectList.split(",")
        self.control_obj_list = [i.strip() for i in self.control_obj_list]
        self.internal_monitor_ioa = self.monitor_ioa
        self.internal_control_ioa = self.control_ioa
        self.device_count = -1

    def create_device(self, quantity, file):
        for iteration in range(quantity):
            self._update_monitor_ioa()
            self._update_control_ioa()
            self.device_count += 1
            for monitor_object in self.monitor_obj_list:
                if monitor_object == 'obj_35m_me_te':
                    obj_info = ObjsInfo.objects.filter(ObjCode=monitor_object).first().ObjInfo
                    sva = Obj35mMeTe.objects.filter(DeviceName=self.name).first().SVA.split(",")
                    if not Obj35mMeTe.objects.filter(DeviceName=self.name).first().Hysteresis:
                        hysteresis = ["1"] * len(sva)
                    else:
                        hysteresis = Obj35mMeTe.objects.filter(DeviceName=self.name).first().Hysteresis.split(",")
                    self._obj_35m_me_te(obj_info, hysteresis, sva, file)
                if monitor_object == 'obj_31m_dp_tb':
                    obj_info = ObjsInfo.objects.filter(ObjCode=monitor_object).first().ObjInfo
                    dpi = Obj31mDpTb.objects.filter(DeviceName=self.name).first().DPI.split(",")
                    self._obj_31m_dp_tb(obj_info, dpi, file)
                if monitor_object == 'obj_30m_sp_tb':
                    obj_info = ObjsInfo.objects.filter(ObjCode=monitor_object).first().ObjInfo
                    spi = Obj30mSpTb.objects.filter(DeviceName=self.name).first().SPI.split(",")
                    self._obj_30m_sp_tb(obj_info, spi, file)
            for control_object in self.control_obj_list:
                if control_object == 'obj_58c_sc_ta':
                    obj_info = ObjsInfo.objects.filter(ObjCode=control_object).first().ObjInfo
                    scs = Obj58cScTa.objects.filter(DeviceName=self.name).first().SCS.split(",")
                    self._obj_58c_sc_ta(obj_info, scs, file)
                if control_object == 'obj_59c_dc_ta':
                    obj_info = ObjsInfo.objects.filter(ObjCode=control_object).first().ObjInfo
                    dcs = Obj59cDcTa.objects.filter(DeviceName=self.name).first().DCS.split(",")
                    self._obj_59c_dc_ta(obj_info, dcs, file)

    def _obj_35m_me_te(self, obj_info, hysteresis, sva, file):
        address = ioa_to_address(self.internal_monitor_ioa)
        object_names = []
        for i in range(len(sva)):
            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_monitor_ioa,
                                      sva[i].format(self.server_iteration, self.device_count).strip(), address[2],
                                      address[1], address[0], hysteresis[i],
                                      sva[i].format(self.server_iteration, self.device_count).strip())

            self.internal_monitor_ioa += 1
            address = update_address(address)
            file.write(xml_obj)
            object_names.append(sva[i].format(self.server_iteration, self.device_count).strip())
        pou.measurements_list.append(object_names)

    def _obj_31m_dp_tb(self, obj_info, dpi, file):
        address = ioa_to_address(self.internal_monitor_ioa)
        object_names = []
        for i in range(len(dpi)):
            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_monitor_ioa,
                                      dpi[i].format(self.server_iteration, 0, self.device_count).strip()
                                      + " / " + dpi[i].format(self.server_iteration, 1, self.device_count).strip(),
                                      address[2], address[1], address[0], dpi[i].format(self.server_iteration,
                                                                                        0, self.device_count).strip(),
                                      dpi[i].format(self.server_iteration, 1, self.device_count).strip())

            self.internal_monitor_ioa += 1
            address = update_address(address)
            file.write(xml_obj)
            object_names.append(dpi[i].format(self.server_iteration, 0, self.device_count).strip())
            object_names.append(dpi[i].format(self.server_iteration, 1, self.device_count).strip())
        pou.states_list.append(object_names)

    def _obj_30m_sp_tb(self, obj_info, spi, file):
        address = ioa_to_address(self.internal_monitor_ioa)
        object_names = []
        for i in range(len(spi)):
            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_monitor_ioa,
                                      spi[i].format(self.server_iteration, self.device_count).strip(),
                                      address[2], address[1], address[0],
                                      spi[i].format(self.server_iteration, self.device_count).strip())

            self.internal_monitor_ioa += 1
            address = update_address(address)
            file.write(xml_obj)
            object_names.append(spi[i].format(self.server_iteration, self.device_count).strip())
        pou.states_list.append(object_names)

    def _obj_58c_sc_ta(self, obj_info, scs, file):
        address = ioa_to_address(self.internal_control_ioa)
        object_names = []
        object_triggers = []
        for i in range(len(scs)):
            command_id = scs[i].format(self.server_iteration, self.device_count).strip()
            command_id_splitted = command_id.split("_")
            trigger = ""
            try:
                if command_id_splitted[5]:
                    trigger = command_id_splitted[2] + "_" + command_id_splitted[3]
            except:
                trigger = command_id_splitted[2]

            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_control_ioa,
                                      command_id, address[2],
                                      address[1], address[0],
                                      command_id, trigger)

            self.internal_control_ioa += 1
            address = update_address(address)
            file.write(xml_obj)
            object_names.append(command_id)
            object_triggers.append(trigger)
        pou.single_commands_list.append(object_names)
        pou.iec_new_message_list.append(object_triggers)

    def _obj_59c_dc_ta(self, obj_info, dcs, file):
        address = ioa_to_address(self.internal_control_ioa)
        object_names = []
        for i in range(len(dcs)):
            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_control_ioa,
                                      dcs[i].format(self.server_iteration, 0, self.device_count).strip() + " / " +
                                      dcs[i].format(self.server_iteration, 1, self.device_count).strip(), address[2],
                                      address[1], address[0],
                                      dcs[i].format(self.server_iteration, 0, self.device_count).strip(),
                                      dcs[i].format(self.server_iteration, 1, self.device_count).strip())

            self.internal_control_ioa += 1
            address = update_address(address)
            file.write(xml_obj)
            object_names.append(dcs[i].format(self.server_iteration, 0, self.device_count).strip())
            object_names.append(dcs[i].format(self.server_iteration, 1, self.device_count).strip())

        pou.double_commands_list.append(object_names)

    def _update_monitor_ioa(self):
        if self.internal_monitor_ioa != self.monitor_ioa:
            self.internal_monitor_ioa = self.monitor_ioa + (self.device_count + 1) * self.monitor_ioa_jump

    def _update_control_ioa(self):
        if self.internal_control_ioa != self.control_ioa:
            self.internal_control_ioa = self.control_ioa + (self.device_count + 1) * self.control_ioa_jump


class ServerCard:
    def __init__(self, name, server_iteration):
        self.name = name
        self.server_iteration = server_iteration
        self.monitor_ioa = Card.objects.filter(Name=name).first().MonitorIoa
        self.monitor_ioa_jump = Card.objects.filter(Name=name).first().MonitorIoaJump
        self.monitor_obj_list = Card.objects.filter(Name=name).first().MonitorObjectList.split(",")
        self.monitor_obj_list = [i.strip() for i in self.monitor_obj_list]
        self.control_ioa = Card.objects.filter(Name=name).first().ControlIoa
        self.control_ioa_jump = Card.objects.filter(Name=name).first().ControlIoaJump
        self.control_obj_list = Card.objects.filter(Name=name).first().ControlObjectList.split(",")
        self.control_obj_list = [i.strip() for i in self.control_obj_list]
        self.internal_monitor_ioa = self.monitor_ioa
        self.internal_control_ioa = self.control_ioa
        self.card_count = -1

    def create_card(self, quantity, file):
        for iteration in range(quantity):
            self._update_monitor_ioa()
            self._update_control_ioa()
            self.card_count += 1
            for monitor_object in self.monitor_obj_list:
                if monitor_object == 'obj_30m_sp_tb':
                    obj_info = ObjsInfo.objects.filter(ObjCode=monitor_object).first().ObjInfo
                    spi = Obj30mSpTb.objects.filter(DeviceName=self.name).first().SPI.split(",")
                    self._obj_30m_sp_tb(obj_info, spi, file)
            for control_object in self.control_obj_list:
                if control_object == 'obj_58c_sc_ta':
                    obj_info = ObjsInfo.objects.filter(ObjCode=control_object).first().ObjInfo
                    scs = Obj58cScTa.objects.filter(DeviceName=self.name).first().SCS.split(",")
                    self._obj_58c_sc_ta(obj_info, scs, file)

    def _obj_30m_sp_tb(self, obj_info, spi, file):
        address = ioa_to_address(self.internal_monitor_ioa)
        for i in range(len(spi)):
            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_monitor_ioa,
                                      spi[i].format(self.server_iteration, (16 * self.card_count) + (i + 1)).strip(),
                                      address[2], address[1], address[0],
                                      spi[i].format(self.server_iteration, (16 * self.card_count) + (i + 1)).strip())

            self.internal_monitor_ioa += 1
            address = update_address(address)
            file.write(xml_obj)

    def _obj_58c_sc_ta(self, obj_info, scs, file):
        address = ioa_to_address(self.internal_control_ioa)
        for i in range(len(scs)):
            xml_obj = obj_info.format(address[0], address[1], address[2], self.internal_control_ioa,
                                      scs[i].format(self.server_iteration, (16 * self.card_count) + (i + 1)).strip(),
                                      address[2], address[1], address[0],
                                      scs[i].format(self.server_iteration, (16 * self.card_count) + (i + 1)).strip(),
                                      "")

            self.internal_control_ioa += 1
            address = update_address(address)
            file.write(xml_obj)

    def _update_monitor_ioa(self):
        if self.internal_monitor_ioa != self.monitor_ioa:
            self.internal_monitor_ioa = self.monitor_ioa + (self.card_count + 1) * self.monitor_ioa_jump

    def _update_control_ioa(self):
        if self.internal_control_ioa != self.control_ioa:
            self.internal_control_ioa = self.control_ioa + (self.card_count + 1) * self.control_ioa_jump
