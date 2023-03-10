from eagle import models, fields, api, SUPERUSER_ID, _
from eagle.exceptions import UserError


class ChangeLockDate(models.TransientModel):
    _name = 'change.lock.date'
    _description = 'Change Lock Date'

    company_id = fields.Many2one('res.company', string="Company",
                                 required=True, default=lambda self: self.env.user.company_id)
    period_lock_date = fields.Date(string='Lock Date for Non-Advisers',
                                   default=lambda self: self.env.user.company_id.period_lock_date,
                                   help='Only users with the Adviser role can edit accounts prior to and '
                                        'inclusive of this date. Use it for period locking inside an open fiscal year')
    fiscalyear_lock_date = fields.Date(string='Lock Date for All Users',
                                       default=lambda self: self.env.user.company_id.fiscalyear_lock_date,
                                       help='No users, including Advisers, can edit accounts prior to and inclusive '
                                            'of this date. Use it for fiscal year locking')

    @api.model
    def default_get(self, vals):
        res = super(ChangeLockDate, self).default_get(vals)
        company_rec = self.env.user.company_id
        res.update({
            'company_id': company_rec.id,
            'period_lock_date': company_rec.period_lock_date,
            'fiscalyear_lock_date': company_rec.fiscalyear_lock_date,
        })
        return res

    @api.multi
    def update_lock_date(self):
        self.ensure_one()
        has_manager_group = self.env.user.has_group('account.group_account_manager')
        if not (has_manager_group or self.env.uid == SUPERUSER_ID):
            raise UserError(_("You Are Not Allowed To Perform This Operation"))
        self.company_id.sudo().write({
            'period_lock_date': self.period_lock_date,
            'fiscalyear_lock_date': self.fiscalyear_lock_date,
        })
