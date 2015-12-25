var IpZapApp = angular.module('IpZapApp', [
    'ngRoute',
    'IpZapControllers',
    'IpZapServices'
]);

// Def of the diferets path in the page
IpZapApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
	when('/control', {
	    templateUrl: 'partials/control.html',
	    controller: 'PlugListCtrl'
	}).
	when('/control/:plugId', {
	    templateUrl: 'partials/plug-detail.html',
	    controller: 'PlugDetailCtrl'
	}).
	otherwise({
	    redirectTo: '/control'
	});
}]);
