# SwiftRiver Gateway WSGI Handler
# ===============================
#
# This file is part of SwiftRiver Gateway.
#
# SwiftRiver Gateway is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# SwiftRiver Gateway is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with SwiftRiver Gateway.  If not, see <http://www.gnu.org/licenses/>.

import os, sys
sys.path.append(os.path.dirname(__file__))
from gateway import app as application