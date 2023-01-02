import 'dart:convert';
import 'dart:typed_data';

import '../../flutter_flow/flutter_flow_util.dart';

import 'api_manager.dart';

export 'api_manager.dart' show ApiCallResponse;

const _kPrivateApiFunctionName = 'ffPrivateApiCall';

class SensorsCall {
  static Future<ApiCallResponse> call() {
    return ApiManager.instance.makeApiCall(
      callName: 'sensors',
      apiUrl: 'https://pg50670-38o1253pnu72raw1.socketxp.com/sensors',
      callType: ApiCallType.GET,
      headers: {},
      params: {},
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
    );
  }

  static dynamic busid(dynamic response) => getJsonField(
        response,
        r'''$.bus_id''',
      );
  static dynamic temp(dynamic response) => getJsonField(
        response,
        r'''$.temperature''',
      );
  static dynamic velocity(dynamic response) => getJsonField(
        response,
        r'''$.velocity''',
      );
}

class ConfluentCall {
  static Future<ApiCallResponse> call() {
    final body = '''
{
  "value": {
    "type": "JSON",
    "data": "Hello World!"
  }
}''';
    return ApiManager.instance.makeApiCall(
      callName: 'confluent',
      apiUrl:
          'https://pkc-41wq6.eu-west-2.aws.confluent.cloud:443/kafka/v3/clusters/lkc-2rj3km/topics/speedometer/records',
      callType: ApiCallType.POST,
      headers: {
        'Content-Type': 'application/json',
        'Authorization':
            'Basic NU1PV1hUSDRVUkhUUVo1WDpiaVNta1B3SGp3Qk1tdjFvMEFvSEZBUWVUSVE3d09KVzNseDJsK3V0MXhNRTdpZ0QxdGd0MzJtclJIS3JaUkVK',
      },
      params: {},
      body: body,
      bodyType: BodyType.JSON,
      returnBody: true,
      encodeBodyUtf8: false,
      decodeUtf8: false,
      cache: false,
    );
  }
}

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
