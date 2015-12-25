/* Controllers */
var IpZapControllers = angular.module('IpZapControllers', []);

IpZapControllers.controller('PlugListCtrl', ['$scope', 'Plug',
    function($scope, Plug) {
	// List all plugs information
	// ==========================
	Plug.ListPlug().$promise.then(function (response) {
	    $scope.plugs = response['plugs'];
	});

	// Change state of a id plug
	// =========================
	$scope.changeState = function(id) {
	    $scope.product = {};
	    // New state
	    $scope.product.state = !$scope.plugs[id]['state'];

	    var product = new Plug($scope.product);
	    product.$UpdatePlug({ id:id });
	};

	// Change Name
	// ===========
	$scope.changeName = function(id, name) {
	    $scope.product = {};
	    $scope.product.name = name;

	    var product = new Plug($scope.product);
	    product.$RenamePlug({ id:id});

	    // Close the modal
	    var modalName = '#modalRename' + id;
	    $(modalName).modal('hide');

	    $scope.plugs[id]['name'] = 'Pepito';
	};

	// Add Alarm
	// =========
	$scope.addAlarm = function(id, date) {
	    $scope.product = {};
	    $scope.product.date = date;

	    var product = new Plug($scope.product);
	    product.$AddAlarm({ id:id });

	    // Close the modal
	    var modalName = '#modalAlarm' + id;
	    $(modalName).modal('hide');
	};

    }]);

IpZapControllers.controller('PlugDetailCtrl', ['$scope', '$routeParams',
    function($scope, $routeParams) {
	$scope.plugId = $routeParams.plugId;
    }]);
