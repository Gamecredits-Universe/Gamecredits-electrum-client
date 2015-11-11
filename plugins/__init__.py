#!/usr/bin/env python
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2015 Thomas Voegtlin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import electrum_gmc as electrum
from electrum_gmc.i18n import _

descriptions = [
    {
        'name': 'audio_modem',
        'fullname': _('Audio MODEM'),
        'description': _('Provides support for air-gapped transaction signing.'),
        'requires': [('amodem', 'http://github.com/romanz/amodem/')],
        'available_for': ['qt'],
    },
    {
        'name': 'btchipwallet',
        'fullname': _('Ledger Wallet'),
        'description': _('Provides support for Ledger hardware wallet'),
        'requires': [('btchip', 'github.com/ledgerhq/btchip-python')],
        'requires_wallet_type': ['btchip'],
        'registers_wallet_type': ('hardware', 'btchip', _("Ledger wallet")),
        'available_for': ['qt', 'cmdline'],
    },
    {
        'name': 'cosigner_pool',
        'fullname': _('Cosigner Pool'),
        'description': ' '.join([
            _("This plugin facilitates the use of multi-signatures wallets."),
            _("It sends and receives partially signed transactions from/to your cosigner wallet."),
            _("Transactions are encrypted and stored on a remote server.")
        ]),
        'requires_wallet_type': ['2of2', '2of3'],
        'available_for': ['qt'],
    },
    {
        'name': 'email_requests',
        'fullname': 'Email',
        'description': _("Send and receive payment request with an email account"),
        'available_for': ['qt'],
    },
    {
        'name': 'exchange_rate',
        'fullname': _("Exchange rates"),
        'description': _("Exchange rates and currency conversion tools."),
        'available_for': ['qt','kivy'],
    },
    {
        'name':'keepkey',
        'fullname': 'KeepKey',
        'description': _('Provides support for KeepKey hardware wallet'),
        'requires': [('keepkeylib','github.com/keepkey/python-keepkey')],
        'requires_wallet_type': ['keepkey'],
        'registers_wallet_type': ('hardware', 'keepkey', _("KeepKey wallet")),
        'available_for': ['qt', 'cmdline'],
    },
    {
        'name': 'labels',
        'fullname': _('LabelSync'),
        'description': '\n'.join([
            _("Synchronize your labels across multiple Electrum installs by using a remote database to save your data. Labels, transactions ids and addresses are encrypted before they are sent to the remote server."),
            _("The label sync's server software is open-source as well and can be found on github.com/maran/electrum-sync-server")
        ]),
        'available_for': ['qt','kivy']
    },
    {
        'name': 'plot',
        'fullname': 'Plot History',
        'description': _("Ability to plot transaction history in graphical mode."),
        'requires': [('matplotlib', 'matplotlib')],
        'available_for': ['qt'],
    },
    {
        'name':'trezor',
        'fullname': 'Trezor Wallet',
        'description': _('Provides support for Trezor hardware wallet'),
        'requires': [('trezorlib','github.com/trezor/python-trezor')],
        'requires_wallet_type': ['trezor'],
        'registers_wallet_type': ('hardware', 'trezor', _("Trezor wallet")),
        'available_for': ['qt', 'cmdline'],
    },
    {
        'name': 'virtualkeyboard',
        'fullname': 'Virtual Keyboard',
        'description': '%s\n%s' % (_("Add an optional virtual keyboard to the password dialog."), _("Warning: do not use this if it makes you pick a weaker password.")),
        'available_for': ['qt'],
    }
]
