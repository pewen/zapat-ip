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
	    // New state
	    $scope.product = {};
	    $scope.product.state = !$scope.plugs[id]['state'];

	    // Make the PUT and update the plugs date
	    var product = new Plug($scope.product);
	    product.$UpdatePlug({ id:id }, function(data){
		$scope.plugs[id] = data.plug;
	    });
	};

	// Change Name
	// ===========
	$scope.changeName = function(id, name) {
	    $scope.product = {};
	    $scope.product.name = name;

	    // Make the PUT and update the plugs date
	    var product = new Plug($scope.product);
	    product.$RenamePlug({ id:id }, function(data){
		$scope.plugs[id]['name'] = data['plug']['name'];
	    });

	    // Close the modal
	    var modalName = '#modalRename' + id;
	    $(modalName).modal('hide');
	};

	// Add Alarm
	// =========
	$scope.addAlarm = function(id, date) {
	    $scope.product = {};
	    $scope.product.date = date;

	    // Make the POST and update the plugs date
	    var product = new Plug($scope.product);
	    product.$AddAlarm({ id:id }, function(data){
		$scope.plugs[id] = data.plug;
	    });

	    // Close the modal
	    var modalName = '#modalAlarm' + id;
	    $(modalName).modal('hide');
	};

    }]);

IpZapControllers.controller('PlugDetailCtrl', ['$scope', '$routeParams',
    function($scope, $routeParams) {
	$scope.plugId = $routeParams.plugId;
    }]);
