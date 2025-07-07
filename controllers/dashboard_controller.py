from models.cliente_model import Cliente
from models.medicos_model import Medico
from models.agendamento_model import Agendamento
from views.dashboard_view import DashboardView

class DashboardController:
    def _init_(self, root):
        self.root = root
        self.view = DashboardView(root, self)

    def iniciar_dashboard(self):
        dados = self._coletar_dados()
        self.view.mostrar(dados)

    def _coletar_dados(self):
        clientes = Cliente.buscar_todos()
        medicos = Medico.buscar_todos()
        agendamentos = Agendamento.buscar_todos()

        total_pendentes = sum(1 for a in agendamentos if a.status.lower() == "pendente")

        return {
            "clientes": len(clientes),
            "medicos": len(medicos),
            "agendamentos": len(agendamentos),
            "pendentes": total_pendentes
        }