# coding: utf-8

from zope.component import adapts
from zope.component import provideAdapter

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

from sboard.categories.interfaces import ICategory
from sboard.factory import getNodeFactory
from sboard.interfaces import INode
from sboard.nodes import CreateView
from sboard.nodes import DetailsView
from sboard.nodes import ListView
from sboard.nodes import NodeView
from sboard.nodes import TagListView

from .forms import LinkIssueForm
from .forms import PolicyIssueForm
from .interfaces import IPolicyIssue
from .interfaces import IVoting


class VotingView(DetailsView):
    adapts(IVoting)

    form = LinkIssueForm

    templates = {
        'details': 'votings/voting_details.html',
    }

    def render(self, overrides=None):
        return super(VotingView, self).render({
            'link_issue_form': LinkIssueForm(),
        })

provideAdapter(VotingView)


class CreatePolicyIssueView(CreateView):
    adapts(object, IPolicyIssue)

    form = PolicyIssueForm

provideAdapter(CreatePolicyIssueView, name="create")

provideAdapter(TagListView, (IPolicyIssue,))


class CreatePolicyIssueLinkView(VotingView):
    adapts(IVoting)

    def render(self):
        if self.request.method == 'POST':
            factory = getNodeFactory('policyissuelink')
            if not self.can('create', factory):
                return render(self.request, '403.html', status=403)

            form = self.get_form(self.request.POST)
            if form.is_valid():
                form.cleaned_data['parent'] = self.node
                child = self.form_save(form, create=True)
                if self.node:
                    return redirect(self.node.permalink())
                else:
                    return redirect(child.permalink())
        else:
            form = self.get_form()

        return super(CreatePolicyIssueLinkView, self).render({
            'link_issue_form': form,
        })

provideAdapter(CreatePolicyIssueLinkView, name="link-policy-issue")


class QuestionGroupView(ListView):
    adapts(ICategory)

    templates = {
        'list': 'votings/question_group.html',
    }

provideAdapter(QuestionGroupView)


class QuickResultsView(NodeView):
    adapts(INode)

    def render(self):
        return HttpResponse(u"""{
    "mps":  [
        {   "name":     "Antanas Nedzinskas",
            "score":    "50",
            "url":      "http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/antanas_nedzinskas.jpg" },
        {   "name":     "Petras Gražulis",
            "score":    "45",
            "url":      "http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/petras_grazulis.jpg" },
        {   "name":     "Česlovas Juršėnas",
            "score":    "42",
            "url":      "http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/ceslovas_jursenas.jpg" }
    ]
}
""")

provideAdapter(QuickResultsView, name='quick-results')


class QuickResultsView(DetailsView):
    adapts(INode)

    templates = {
        'details': 'votings/results.html',
    }

    def render(self):
        return super(QuickResultsView, self).render({
            'results': [
                {'name': u'Eligijus Masiulis',
                 'score': 86,
                 'url': 'http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/eligijus_masiulis.jpg',
                },
                {'name': u'Irena Degutienė',
                 'score': 85,
                 'url': 'http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/irena_degutiene.jpg',
                },
                {'name': u'Vytautas Gapšys',
                 'score': 79,
                 'url': 'http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/vytautas_gapsys.jpg',
                },
                {'name': u'Algirdas Sysas',
                 'score': 76,
                 'url': 'http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/algirdas_sysas.jpg',
                },
                {'name': u'Remigijus Žemaitaitis',
                 'score': 69,
                 'url': 'http://www3.lrs.lt/home/seimo_nariu_nuotraukos/2008/remigijus_zemaitaitis.jpg',
                }
            ],
            'party_results': [
                {'name': u'Tėvynės sąjungos-Lietuvos krikščionių demokratų frakcija',
                 'score':  78,
                 'url':    'http://manobalsas.lt/politikai/logos/part_37.gif',
                },
                {'name': u'Lietuvos socialdemokratų partijos frakcija',
                 'score':  72,
                 'url':    'http://manobalsas.lt/politikai/logos/part_20.gif',
                },
                {'name': u'Liberalų ir centro sąjungos frakcija',
                 'score':  67,
                 'url':    'http://manobalsas.lt/politikai/logos/part_3.gif',
                },
                {'name': u'Liberalų sąjūdžio frakcija',
                 'score':  66,
                 'url':    'http://manobalsas.lt/politikai/logos/part_18.gif',
                },
                {'name': u'Frakcija "Tvarka ir teisingumas"',
                 'score':  56,
                 'url':    'http://manobalsas.lt/politikai/logos/part_30.gif',
                },
            ],
        })

provideAdapter(QuickResultsView, name='results')
