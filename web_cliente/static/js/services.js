var IpZapServices = angular.module('IpZapServices', ['ngResource']);

IpZapServices.factory('Plug', ['$resource', function($resource) {
    return $resource('http://localhost:8003/api/plugs/:id/:cmd',
		     {id : "@id", cmd : "@cmd"},
		     {
			 'ListPlug': {
			     method: 'GET',
			     isArray: false
			 },
			 'UpdatePlug': {
			     method: 'PUT',
			     params: { cmd:"state" },
			 },
			 'RenamePlug': {
			     method: 'PUT',
			 },
			 'AddAlarm': {
			     method: 'POST'
			 },
			 'DeleteAlarm': {
			     method: 'DELETE'
			 }
		     });
}]);
