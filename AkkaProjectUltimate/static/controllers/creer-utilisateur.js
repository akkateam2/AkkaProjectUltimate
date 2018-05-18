app.controller('creer-utilisateur', function($scope, $http, $location) {
    $scope.superieur_liste = null;

    $scope.clickChoixType = function () {
        if(($scope.type=="Business Manager")||($scope.type=="Chargé de recrutement")){
            $http({
                method: 'GET',
                params: {
                    "type": $scope.type
                },
                url: "/akkannuaire/api/test"
            }).then(function successCallback(response) {
                $scope.superieur_liste = response.data.superieurs;
            }, function errorCallback(response) {
                console.log(response);
            });
        }
    };

    $scope.clickChoixSuperieur = function (superieur) {

        console.log($scope.superieurModel);
        $scope.superieurModel = superieur.id
        console.log($scope.superieurModel);
    };
});