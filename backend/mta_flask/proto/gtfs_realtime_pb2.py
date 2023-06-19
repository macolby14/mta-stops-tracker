# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mta_flask/proto/gtfs-realtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n#mta_flask/proto/gtfs-realtime.proto\x12\x10transit_realtime"q\n\x0b\x46\x65\x65\x64Message\x12,\n\x06header\x18\x01 \x02(\x0b\x32\x1c.transit_realtime.FeedHeader\x12,\n\x06\x65ntity\x18\x02 \x03(\x0b\x32\x1c.transit_realtime.FeedEntity*\x06\x08\xe8\x07\x10\xd0\x0f"\xcf\x01\n\nFeedHeader\x12\x1d\n\x15gtfs_realtime_version\x18\x01 \x02(\t\x12Q\n\x0eincrementality\x18\x02 \x01(\x0e\x32+.transit_realtime.FeedHeader.Incrementality:\x0c\x46ULL_DATASET\x12\x11\n\ttimestamp\x18\x03 \x01(\x04"4\n\x0eIncrementality\x12\x10\n\x0c\x46ULL_DATASET\x10\x00\x12\x10\n\x0c\x44IFFERENTIAL\x10\x01*\x06\x08\xe8\x07\x10\xd0\x0f"\xca\x01\n\nFeedEntity\x12\n\n\x02id\x18\x01 \x02(\t\x12\x19\n\nis_deleted\x18\x02 \x01(\x08:\x05\x66\x61lse\x12\x31\n\x0btrip_update\x18\x03 \x01(\x0b\x32\x1c.transit_realtime.TripUpdate\x12\x32\n\x07vehicle\x18\x04 \x01(\x0b\x32!.transit_realtime.VehiclePosition\x12&\n\x05\x61lert\x18\x05 \x01(\x0b\x32\x17.transit_realtime.Alert*\x06\x08\xe8\x07\x10\xd0\x0f"\x9a\x05\n\nTripUpdate\x12.\n\x04trip\x18\x01 \x02(\x0b\x32 .transit_realtime.TripDescriptor\x12\x34\n\x07vehicle\x18\x03 \x01(\x0b\x32#.transit_realtime.VehicleDescriptor\x12\x45\n\x10stop_time_update\x18\x02 \x03(\x0b\x32+.transit_realtime.TripUpdate.StopTimeUpdate\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\r\n\x05\x64\x65lay\x18\x05 \x01(\x05\x1aI\n\rStopTimeEvent\x12\r\n\x05\x64\x65lay\x18\x01 \x01(\x05\x12\x0c\n\x04time\x18\x02 \x01(\x03\x12\x13\n\x0buncertainty\x18\x03 \x01(\x05*\x06\x08\xe8\x07\x10\xd0\x0f\x1a\xe9\x02\n\x0eStopTimeUpdate\x12\x15\n\rstop_sequence\x18\x01 \x01(\r\x12\x0f\n\x07stop_id\x18\x04 \x01(\t\x12;\n\x07\x61rrival\x18\x02 \x01(\x0b\x32*.transit_realtime.TripUpdate.StopTimeEvent\x12=\n\tdeparture\x18\x03 \x01(\x0b\x32*.transit_realtime.TripUpdate.StopTimeEvent\x12j\n\x15schedule_relationship\x18\x05 \x01(\x0e\x32@.transit_realtime.TripUpdate.StopTimeUpdate.ScheduleRelationship:\tSCHEDULED"?\n\x14ScheduleRelationship\x12\r\n\tSCHEDULED\x10\x00\x12\x0b\n\x07SKIPPED\x10\x01\x12\x0b\n\x07NO_DATA\x10\x02*\x06\x08\xe8\x07\x10\xd0\x0f*\x06\x08\xe8\x07\x10\xd0\x0f"\xe0\x06\n\x0fVehiclePosition\x12.\n\x04trip\x18\x01 \x01(\x0b\x32 .transit_realtime.TripDescriptor\x12\x34\n\x07vehicle\x18\x08 \x01(\x0b\x32#.transit_realtime.VehicleDescriptor\x12,\n\x08position\x18\x02 \x01(\x0b\x32\x1a.transit_realtime.Position\x12\x1d\n\x15\x63urrent_stop_sequence\x18\x03 \x01(\r\x12\x0f\n\x07stop_id\x18\x07 \x01(\t\x12Z\n\x0e\x63urrent_status\x18\x04 \x01(\x0e\x32\x33.transit_realtime.VehiclePosition.VehicleStopStatus:\rIN_TRANSIT_TO\x12\x11\n\ttimestamp\x18\x05 \x01(\x04\x12K\n\x10\x63ongestion_level\x18\x06 \x01(\x0e\x32\x31.transit_realtime.VehiclePosition.CongestionLevel\x12K\n\x10occupancy_status\x18\t \x01(\x0e\x32\x31.transit_realtime.VehiclePosition.OccupancyStatus"G\n\x11VehicleStopStatus\x12\x0f\n\x0bINCOMING_AT\x10\x00\x12\x0e\n\nSTOPPED_AT\x10\x01\x12\x11\n\rIN_TRANSIT_TO\x10\x02"}\n\x0f\x43ongestionLevel\x12\x1c\n\x18UNKNOWN_CONGESTION_LEVEL\x10\x00\x12\x14\n\x10RUNNING_SMOOTHLY\x10\x01\x12\x0f\n\x0bSTOP_AND_GO\x10\x02\x12\x0e\n\nCONGESTION\x10\x03\x12\x15\n\x11SEVERE_CONGESTION\x10\x04"\xaf\x01\n\x0fOccupancyStatus\x12\t\n\x05\x45MPTY\x10\x00\x12\x18\n\x14MANY_SEATS_AVAILABLE\x10\x01\x12\x17\n\x13\x46\x45W_SEATS_AVAILABLE\x10\x02\x12\x16\n\x12STANDING_ROOM_ONLY\x10\x03\x12\x1e\n\x1a\x43RUSHED_STANDING_ROOM_ONLY\x10\x04\x12\x08\n\x04\x46ULL\x10\x05\x12\x1c\n\x18NOT_ACCEPTING_PASSENGERS\x10\x06*\x06\x08\xe8\x07\x10\xd0\x0f"\xb6\x06\n\x05\x41lert\x12\x32\n\ractive_period\x18\x01 \x03(\x0b\x32\x1b.transit_realtime.TimeRange\x12\x39\n\x0finformed_entity\x18\x05 \x03(\x0b\x32 .transit_realtime.EntitySelector\x12;\n\x05\x63\x61use\x18\x06 \x01(\x0e\x32\x1d.transit_realtime.Alert.Cause:\rUNKNOWN_CAUSE\x12>\n\x06\x65\x66\x66\x65\x63t\x18\x07 \x01(\x0e\x32\x1e.transit_realtime.Alert.Effect:\x0eUNKNOWN_EFFECT\x12/\n\x03url\x18\x08 \x01(\x0b\x32".transit_realtime.TranslatedString\x12\x37\n\x0bheader_text\x18\n \x01(\x0b\x32".transit_realtime.TranslatedString\x12<\n\x10\x64\x65scription_text\x18\x0b \x01(\x0b\x32".transit_realtime.TranslatedString"\xd8\x01\n\x05\x43\x61use\x12\x11\n\rUNKNOWN_CAUSE\x10\x01\x12\x0f\n\x0bOTHER_CAUSE\x10\x02\x12\x15\n\x11TECHNICAL_PROBLEM\x10\x03\x12\n\n\x06STRIKE\x10\x04\x12\x11\n\rDEMONSTRATION\x10\x05\x12\x0c\n\x08\x41\x43\x43IDENT\x10\x06\x12\x0b\n\x07HOLIDAY\x10\x07\x12\x0b\n\x07WEATHER\x10\x08\x12\x0f\n\x0bMAINTENANCE\x10\t\x12\x10\n\x0c\x43ONSTRUCTION\x10\n\x12\x13\n\x0fPOLICE_ACTIVITY\x10\x0b\x12\x15\n\x11MEDICAL_EMERGENCY\x10\x0c"\xb5\x01\n\x06\x45\x66\x66\x65\x63t\x12\x0e\n\nNO_SERVICE\x10\x01\x12\x13\n\x0fREDUCED_SERVICE\x10\x02\x12\x16\n\x12SIGNIFICANT_DELAYS\x10\x03\x12\n\n\x06\x44\x45TOUR\x10\x04\x12\x16\n\x12\x41\x44\x44ITIONAL_SERVICE\x10\x05\x12\x14\n\x10MODIFIED_SERVICE\x10\x06\x12\x10\n\x0cOTHER_EFFECT\x10\x07\x12\x12\n\x0eUNKNOWN_EFFECT\x10\x08\x12\x0e\n\nSTOP_MOVED\x10\t*\x06\x08\xe8\x07\x10\xd0\x0f"/\n\tTimeRange\x12\r\n\x05start\x18\x01 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x04*\x06\x08\xe8\x07\x10\xd0\x0f"i\n\x08Position\x12\x10\n\x08latitude\x18\x01 \x02(\x02\x12\x11\n\tlongitude\x18\x02 \x02(\x02\x12\x0f\n\x07\x62\x65\x61ring\x18\x03 \x01(\x02\x12\x10\n\x08odometer\x18\x04 \x01(\x01\x12\r\n\x05speed\x18\x05 \x01(\x02*\x06\x08\xe8\x07\x10\xd0\x0f"\xa0\x02\n\x0eTripDescriptor\x12\x0f\n\x07trip_id\x18\x01 \x01(\t\x12\x10\n\x08route_id\x18\x05 \x01(\t\x12\x14\n\x0c\x64irection_id\x18\x06 \x01(\r\x12\x12\n\nstart_time\x18\x02 \x01(\t\x12\x12\n\nstart_date\x18\x03 \x01(\t\x12T\n\x15schedule_relationship\x18\x04 \x01(\x0e\x32\x35.transit_realtime.TripDescriptor.ScheduleRelationship"O\n\x14ScheduleRelationship\x12\r\n\tSCHEDULED\x10\x00\x12\t\n\x05\x41\x44\x44\x45\x44\x10\x01\x12\x0f\n\x0bUNSCHEDULED\x10\x02\x12\x0c\n\x08\x43\x41NCELED\x10\x03*\x06\x08\xe8\x07\x10\xd0\x0f"M\n\x11VehicleDescriptor\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x15\n\rlicense_plate\x18\x03 \x01(\t*\x06\x08\xe8\x07\x10\xd0\x0f"\x92\x01\n\x0e\x45ntitySelector\x12\x11\n\tagency_id\x18\x01 \x01(\t\x12\x10\n\x08route_id\x18\x02 \x01(\t\x12\x12\n\nroute_type\x18\x03 \x01(\x05\x12.\n\x04trip\x18\x04 \x01(\x0b\x32 .transit_realtime.TripDescriptor\x12\x0f\n\x07stop_id\x18\x05 \x01(\t*\x06\x08\xe8\x07\x10\xd0\x0f"\x96\x01\n\x10TranslatedString\x12\x43\n\x0btranslation\x18\x01 \x03(\x0b\x32..transit_realtime.TranslatedString.Translation\x1a\x35\n\x0bTranslation\x12\x0c\n\x04text\x18\x01 \x02(\t\x12\x10\n\x08language\x18\x02 \x01(\t*\x06\x08\xe8\x07\x10\xd0\x0f*\x06\x08\xe8\x07\x10\xd0\x0f\x42\x46\n\x1b\x63om.google.transit.realtimeZ\'github.com/google/transit/gtfs-realtime'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "mta_flask.proto.gtfs_realtime_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = (
        b"\n\033com.google.transit.realtimeZ'github.com/google/transit/gtfs-realtime"
    )
    _FEEDMESSAGE._serialized_start = 57
    _FEEDMESSAGE._serialized_end = 170
    _FEEDHEADER._serialized_start = 173
    _FEEDHEADER._serialized_end = 380
    _FEEDHEADER_INCREMENTALITY._serialized_start = 320
    _FEEDHEADER_INCREMENTALITY._serialized_end = 372
    _FEEDENTITY._serialized_start = 383
    _FEEDENTITY._serialized_end = 585
    _TRIPUPDATE._serialized_start = 588
    _TRIPUPDATE._serialized_end = 1254
    _TRIPUPDATE_STOPTIMEEVENT._serialized_start = 809
    _TRIPUPDATE_STOPTIMEEVENT._serialized_end = 882
    _TRIPUPDATE_STOPTIMEUPDATE._serialized_start = 885
    _TRIPUPDATE_STOPTIMEUPDATE._serialized_end = 1246
    _TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP._serialized_start = 1175
    _TRIPUPDATE_STOPTIMEUPDATE_SCHEDULERELATIONSHIP._serialized_end = 1238
    _VEHICLEPOSITION._serialized_start = 1257
    _VEHICLEPOSITION._serialized_end = 2121
    _VEHICLEPOSITION_VEHICLESTOPSTATUS._serialized_start = 1737
    _VEHICLEPOSITION_VEHICLESTOPSTATUS._serialized_end = 1808
    _VEHICLEPOSITION_CONGESTIONLEVEL._serialized_start = 1810
    _VEHICLEPOSITION_CONGESTIONLEVEL._serialized_end = 1935
    _VEHICLEPOSITION_OCCUPANCYSTATUS._serialized_start = 1938
    _VEHICLEPOSITION_OCCUPANCYSTATUS._serialized_end = 2113
    _ALERT._serialized_start = 2124
    _ALERT._serialized_end = 2946
    _ALERT_CAUSE._serialized_start = 2538
    _ALERT_CAUSE._serialized_end = 2754
    _ALERT_EFFECT._serialized_start = 2757
    _ALERT_EFFECT._serialized_end = 2938
    _TIMERANGE._serialized_start = 2948
    _TIMERANGE._serialized_end = 2995
    _POSITION._serialized_start = 2997
    _POSITION._serialized_end = 3102
    _TRIPDESCRIPTOR._serialized_start = 3105
    _TRIPDESCRIPTOR._serialized_end = 3393
    _TRIPDESCRIPTOR_SCHEDULERELATIONSHIP._serialized_start = 3306
    _TRIPDESCRIPTOR_SCHEDULERELATIONSHIP._serialized_end = 3385
    _VEHICLEDESCRIPTOR._serialized_start = 3395
    _VEHICLEDESCRIPTOR._serialized_end = 3472
    _ENTITYSELECTOR._serialized_start = 3475
    _ENTITYSELECTOR._serialized_end = 3621
    _TRANSLATEDSTRING._serialized_start = 3624
    _TRANSLATEDSTRING._serialized_end = 3774
    _TRANSLATEDSTRING_TRANSLATION._serialized_start = 3713
    _TRANSLATEDSTRING_TRANSLATION._serialized_end = 3766
# @@protoc_insertion_point(module_scope)
