var pollControllers = angular.module('pollControllers', []);

pollsControllers.controller('PollListCtrl', ['$scope', 'Poll',
  function($scope, Poll) {
    $scope.id = Poll.query();
  }]);

pollsControllers.controller('PollDetailCtrl', ['$scope', 'Poll',
  function($scope, Poll) {
}]);