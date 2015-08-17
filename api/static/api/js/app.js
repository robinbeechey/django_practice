'use strict';

/* App Module */

var pollApp = angular.module('pollApp', [
  'ngRoute',
  'pollsControllers',
  'pollsServices'
]);

phonecatApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/questions', {
        templateUrl: 'http://localhost:7000/api/questions/',
        controller: 'PollListController'
      }).
      when('/questions/:id', {
        templateUrl: 'http://localhost:7000/api/questions/:id',
        controller: 'PollListController'
      }).
      otherwise({
        redirectTo: '/questions'
      });
  }]);
