from xml.etree import ElementTree

from esoc_events.utils.time import fdyn_to_iso, iso_to_fdyn
from esoc_events.utils.xml import xml_to_obj


def test_fdyn_to_iso() -> None:
    doy_utc = "2023-104T12:47:12.000Z"
    assert fdyn_to_iso(doy_utc) == "2023-04-14T12:47:12.000Z"


def test_iso_to_fdyn() -> None:
    doy_utc = "2023-104T12:47:12.000Z"
    iso_utc = "2023-04-14T12:47:12.000Z"
    assert iso_to_fdyn(iso_utc) == doy_utc


def test_xml_to_obj() -> None:
    element = ElementTree.fromstring(
        """<service_session>
      <osg_dn>XMM_Routine_1.xmm_orbit_com.nominal_definition.XMM</osg_dn>
      <satellite_id>XMM</satellite_id>
      <ground_station>KRU</ground_station>
      <activity_start>2024-02-21T06:00:20.000Z</activity_start>
      <activity_end>2024-02-22T04:45:18.000Z</activity_end>
      <tracking_start>2024-02-21T06:45:20.000Z</tracking_start>
      <tracking_end>2024-02-22T04:30:18.000Z</tracking_end>
      <oss_ref>EVENT-2023.339.12.16.51.589755-796414</oss_ref>
      <comment><![CDATA[ESOC MCP]]></comment>
      <service_instance>
        <ssi_id>EVENT-2024.052.15.21.56.717342-2475328</ssi_id>
        <service_type>telemetryReception</service_type>
        <activity_start>2024-02-21T06:45:20.000Z</activity_start>
        <activity_end>2024-02-22T04:30:18.000Z</activity_end>
      </service_instance>
      <service_instance>
        <ssi_id>EVENT-2024.052.15.21.56.718156-2475329</ssi_id>
        <service_type>telecommandUplink</service_type>
        <activity_start>2024-02-21T06:45:20.000Z</activity_start>
        <activity_end>2024-02-22T04:30:18.000Z</activity_end>
      </service_instance>
    </service_session>
"""
    )
    json = xml_to_obj(element)
    assert json.get("service_session").get("satellite_id") == "XMM"
