from django.shortcuts import redirect
from django.urls import reverse

class RoleNavigationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            role = request.user.role
            if role == 'admin':
                # Modification de la navigation pour l'administrateur
                # Exemple de code pour modifier la navigation
                request.admin_navigation = True
            elif role == 'web':
                # Modification de la navigation pour l'utilisateur web
                # Exemple de code pour modifier la navigation
                request.web_navigation = True
            elif role == 'stock':
                # Modification de la navigation pour l'utilisateur avec le rôle stock
                # Exemple de code pour modifier la navigation
                request.stock_navigation = True
            elif role == 'membre':
                # Modification de la navigation pour l'utilisateur membre
                # Exemple de code pour modifier la navigation
                request.membre_navigation = True
        else:
            # Redirection si l'utilisateur n'est pas authentifié
            return redirect(reverse('login'))
        
        response = self.get_response(request)
        return response
