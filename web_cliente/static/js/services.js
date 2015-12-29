var IpZapServices = angular.module('IpZapServices', ['ngResource']);

IpZapServices.factory('Plug', ['$resource', function($resource) {
    return $resource('http://localhost:8003/api/plugs/:id/:cmd',
		     {id : "@id", cmd : "@cmd"},
		     {
			 'ListPlug': {
			     method: 'GET',
			     format: 'json',
			     isArray: false
			 },
			 'UpdatePlug': {
			     method: 'PUT',
			     params: { cmd:"state" },
			     format: 'json',
			     isArray: false
			 },
			 'RenamePlug': {
			     method: 'PUT',
			     format: 'json',
			     isArray: false
			 },
			 'AddAlarm': {
			     method: 'POST',
			     format: 'json',
			     isArray: false
			 },
			 'DeleteAlarm': {
			     method: 'DELETE',
			     format: 'json',
			     isArray: false
			 }
		     });
}]);
