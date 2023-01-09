import 'dart:convert';
import 'dart:typed_data';

import '../../flutter_flow/flutter_flow_util.dart';

import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

const _kPrivateApiFunctionName = 'ffPrivateApiCall';

/// Start bus Group Code

class BusGroup {
  static String baseUrl = 'https://pg50670-38o1253pnu72raw1.socketxp.com';
  static Map<String, String> headers = {};
  static SensorsCall sensorsCall = SensorsCall();
  static NewticketCall newticketCall = NewticketCall();
}

class SensorsCall {
  Future<ApiCallResponse> call() {
    return ApiManager.instance.makeApiCall(
      callName: 'sensors',
      apiUrl: '${BusGroup.baseUrl}/sensors',
      callType: ApiCallType.GET,
      headers: {
        ...BusGroup.headers,
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
    );
  }

  dynamic busid(dynamic response) => getJsonField(
        response,
        r'''$.bus_id''',
      );
  dynamic temp(dynamic response) => getJsonField(
        response,
        r'''$.temperature''',
      );
  dynamic velocity(dynamic response) => getJsonField(
        response,
        r'''$.velocity''',
      );
  dynamic ticketnum(dynamic response) => getJsonField(
        response,
        r'''$.ticket_num''',
      );
}

class NewticketCall {
  Future<ApiCallResponse> call() {
    return ApiManager.instance.makeApiCall(
      callName: 'newticket',
      apiUrl: '${BusGroup.baseUrl}/newticket',
      callType: ApiCallType.GET,
      headers: {
        ...BusGroup.headers,
      },
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
    );
  }

  dynamic newticket(dynamic response) => getJsonField(
        response,
        r'''$.new_ticket''',
      );
}

/// End bus Group Code

class ApiPagingParams {
  int nextPageNumber = 0;
  int numItems = 0;
  dynamic lastResponse;

  ApiPagingParams({
    required this.nextPageNumber,
    required this.numItems,
    required this.lastResponse,
  });

  @override
  String toString() =>
      'PagingParams(nextPageNumber: $nextPageNumber, numItems: $numItems, lastResponse: $lastResponse,)';
}

String _serializeList(List? list) {
  list ??= <String>[];
  try {
    return json.encode(list);
  } catch (_) {
    return '[]';
  }
}

String _serializeJson(dynamic jsonVar) {
  jsonVar ??= {};
  try {
    return json.encode(jsonVar);
  } catch (_) {
    return '{}';
  }
}
