from eagle import api, fields
from eagle.tests import tagged
from eagle.addons.account.tests.account_test_classes import AccountingTestCase


@tagged('post_install', '-at_install')
class TestReconciliationHeavyLoad(AccountingTestCase):
    """Check that reconciliation can be done for a move with many lines
    """

    def _create_move(self, journal):
        values = {
            'ref': "Test reconcile - Auto-generated by script",
            'journal_id': journal.id,
            'state': 'draft',
            'company_id': journal.env.user.company_id.id,
        }
        return journal.env['account.move'].create(values)

    def _get_values_account_move_line(
            self, account, journal, name, move,
            credit=0, debit=0, date=fields.Date.today()):
        return {
            'journal_id': journal.id,
            'name': name,
            'account_id': account.id,
            'move_id': move.id,
            'quantity': 1,
            'credit': credit,
            'debit': debit,
            'date': date,
        }

    def setUp(self):
        super(TestReconciliationHeavyLoad, self).setUp()

        self.account_type = self.env.ref('account.data_account_type_receivable')

        self.journal = self.env['account.journal'].search([
            ('type', '=', 'bank'),
            ('company_id', '=', self.env.user.company_id.id),
        ], limit=1)

        self.account = self.env['account.account'].search([
            ('user_type_id', '=', self.account_type.id),
            ('company_id', '=', self.env.user.company_id.id),
        ], limit=1)

    def test_heavy_load_reconciliation(self):
        """Does reconciliation on a move with nb_lines lines.
           To avoid burdening uselessly the runbot, we only set nb_lines to 10,
           but it should be of order 10^3 to be meaningful.
           The day we manage to use system build settings to execute tests
           this could be done automatically for "heavy load builds",
           but for now this should be changed manually.
        """

        total = 0
        line_ids = []
        amount_per_line = 1
        nb_lines = 10  # change this to 1000 or more
        move = self._create_move(self.journal)

        for i in range(nb_lines):
            name = "Move line credit #%s" % i
            total += amount_per_line
            values = self._get_values_account_move_line(
                self.account, self.journal, name, move, credit=amount_per_line)
            line_ids.append((0, False, values))

        values = self._get_values_account_move_line(
            self.account, self.journal, "Move line Debit", move, debit=total)
        line_ids.append((0, False, values))

        move.write({'line_ids': line_ids})

        move.line_ids.reconcile()

        self.assertTrue(all(move.line_ids.mapped('reconciled')))
