"""IRC control message."""

import re
from enum import Enum, unique
from typing import Optional

from irc.messages.base import IRCBaseMessage

# Taken from https://www.alien.net.au/irc/irc2numerics.html
# using the following script:
# copy(
#  Array.from(document.querySelectorAll('tr'))
#   .filter(x => x.children[2].textContent.includes('RFC'))
#   .map(x => `${x.children[1].textContent.trim()} = "${x.children[0].textContent.trim()}"`)
#   .join('\n')
# )

# Regex for matching the individual parts of an IRC message
control_message_regex = re.compile("^:([^ ]+) ([0-9]+) ([^ ]+)( ([^ ]+) )(.*)$")


@unique
class IRCControlMessageType(Enum):
    """IRC message types."""

    RPL_WELCOME = "001"
    RPL_YOURHOST = "002"
    RPL_CREATED = "003"
    RPL_MYINFO = "004"
    RPL_BOUNCE = "005"
    RPL_TRACELINK = "200"
    RPL_TRACECONNECTING = "201"
    RPL_TRACEHANDSHAKE = "202"
    RPL_TRACEUNKNOWN = "203"
    RPL_TRACEOPERATOR = "204"
    RPL_TRACEUSER = "205"
    RPL_TRACESERVER = "206"
    RPL_TRACESERVICE = "207"
    RPL_TRACENEWTYPE = "208"
    RPL_TRACECLASS = "209"
    RPL_TRACERECONNECT = "210"
    RPL_STATSLINKINFO = "211"
    RPL_STATSCOMMANDS = "212"
    RPL_STATSCLINE = "213"
    RPL_STATSNLINE = "214"
    RPL_STATSILINE = "215"
    RPL_STATSKLINE = "216"
    RPL_STATSQLINE = "217"
    RPL_STATSYLINE = "218"
    RPL_ENDOFSTATS = "219"
    RPL_UMODEIS = "221"
    RPL_SERVICEINFO = "231"
    RPL_ENDOFSERVICES = "232"
    RPL_SERVICE = "233"
    RPL_SERVLIST = "234"
    RPL_SERVLISTEND = "235"
    RPL_STATSVLINE = "240"
    RPL_STATSLLINE = "241"
    RPL_STATSUPTIME = "242"
    RPL_STATSOLINE = "243"
    RPL_STATSHLINE = "244"
    RPL_STATSPING = "246"
    RPL_STATSBLINE = "247"
    RPL_STATSDLINE = "250"
    RPL_LUSERCLIENT = "251"
    RPL_LUSEROP = "252"
    RPL_LUSERUNKNOWN = "253"
    RPL_LUSERCHANNELS = "254"
    RPL_LUSERME = "255"
    RPL_ADMINME = "256"
    RPL_ADMINLOC1 = "257"
    RPL_ADMINLOC2 = "258"
    RPL_ADMINEMAIL = "259"
    RPL_TRACELOG = "261"
    RPL_TRACEEND = "262"
    RPL_TRYAGAIN = "263"
    RPL_NONE = "300"
    RPL_AWAY = "301"
    RPL_USERHOST = "302"
    RPL_ISON = "303"
    RPL_UNAWAY = "305"
    RPL_NOWAWAY = "306"
    RPL_WHOISUSER = "311"
    RPL_WHOISSERVER = "312"
    RPL_WHOISOPERATOR = "313"
    RPL_WHOWASUSER = "314"
    RPL_ENDOFWHO = "315"
    RPL_WHOISCHANOP = "316"
    RPL_WHOISIDLE = "317"
    RPL_ENDOFWHOIS = "318"
    RPL_WHOISCHANNELS = "319"
    RPL_LISTSTART = "321"
    RPL_LIST = "322"
    RPL_LISTEND = "323"
    RPL_CHANNELMODEIS = "324"
    RPL_UNIQOPIS = "325"
    RPL_NOTOPIC = "331"
    RPL_TOPIC = "332"
    RPL_INVITING = "341"
    RPL_SUMMONING = "342"
    RPL_INVITELIST = "346"
    RPL_ENDOFINVITELIST = "347"
    RPL_EXCEPTLIST = "348"
    RPL_ENDOFEXCEPTLIST = "349"
    RPL_VERSION = "351"
    RPL_WHOREPLY = "352"
    RPL_NAMREPLY = "353"
    RPL_KILLDONE = "361"
    RPL_CLOSING = "362"
    RPL_CLOSEEND = "363"
    RPL_LINKS = "364"
    RPL_ENDOFLINKS = "365"
    RPL_ENDOFNAMES = "366"
    RPL_BANLIST = "367"
    RPL_ENDOFBANLIST = "368"
    RPL_ENDOFWHOWAS = "369"
    RPL_INFO = "371"
    RPL_MOTD = "372"
    RPL_INFOSTART = "373"
    RPL_ENDOFINFO = "374"
    RPL_MOTDSTART = "375"
    RPL_ENDOFMOTD = "376"
    RPL_YOUREOPER = "381"
    RPL_REHASHING = "382"
    RPL_YOURESERVICE = "383"
    RPL_MYPORTIS = "384"
    RPL_TIME = "391"
    RPL_USERSSTART = "392"
    RPL_USERS = "393"
    RPL_ENDOFUSERS = "394"
    RPL_NOUSERS = "395"
    ERR_NOSUCHNICK = "401"
    ERR_NOSUCHSERVER = "402"
    ERR_NOSUCHCHANNEL = "403"
    ERR_CANNOTSENDTOCHAN = "404"
    ERR_TOOMANYCHANNELS = "405"
    ERR_WASNOSUCHNICK = "406"
    ERR_TOOMANYTARGETS = "407"
    ERR_NOSUCHSERVICE = "408"
    ERR_NOORIGIN = "409"
    ERR_NORECIPIENT = "411"
    ERR_NOTEXTTOSEND = "412"
    ERR_NOTOPLEVEL = "413"
    ERR_WILDTOPLEVEL = "414"
    ERR_BADMASK = "415"
    ERR_UNKNOWNCOMMAND = "421"
    ERR_NOMOTD = "422"
    ERR_NOADMININFO = "423"
    ERR_FILEERROR = "424"
    ERR_NONICKNAMEGIVEN = "431"
    ERR_ERRONEUSNICKNAME = "432"
    ERR_NICKNAMEINUSE = "433"
    ERR_NICKCOLLISION = "436"
    ERR_UNAVAILRESOURCE = "437"
    ERR_USERNOTINCHANNEL = "441"
    ERR_NOTONCHANNEL = "442"
    ERR_USERONCHANNEL = "443"
    ERR_NOLOGIN = "444"
    ERR_SUMMONDISABLED = "445"
    ERR_USERSDISABLED = "446"
    ERR_NOTREGISTERED = "451"
    ERR_NEEDMOREPARAMS = "461"
    ERR_ALREADYREGISTERED = "462"
    ERR_NOPERMFORHOST = "463"
    ERR_PASSWDMISMATCH = "464"
    ERR_YOUREBANNEDCREEP = "465"
    ERR_YOUWILLBEBANNED = "466"
    ERR_KEYSET = "467"
    ERR_CHANNELISFULL = "471"
    ERR_UNKNOWNMODE = "472"
    ERR_INVITEONLYCHAN = "473"
    ERR_BANNEDFROMCHAN = "474"
    ERR_BADCHANNELKEY = "475"
    ERR_BADCHANMASK = "476"
    ERR_NOCHANMODES = "477"
    ERR_BANLISTFULL = "478"
    ERR_NOPRIVILEGES = "481"
    ERR_CHANOPRIVSNEEDED = "482"
    ERR_CANTKILLSERVER = "483"
    ERR_RESTRICTED = "484"
    ERR_UNIQOPRIVSNEEDED = "485"
    ERR_NOOPERHOST = "491"
    ERR_NOSERVICEHOST = "492"
    ERR_UMODEUNKNOWNFLAG = "501"
    ERR_USERSDONTMATCH = "502"


class IRCControlMessage(IRCBaseMessage):
    """An IRC control message."""

    def __init__(  # pylint: disable=too-many-arguments
            self,
            raw_message: str,
            server: str,
            message_type: IRCControlMessageType,
            target: str,
            parameter: Optional[str],
            message: str
    ) -> None:
        super().__init__(raw_message)

        self.__server = server
        self.__message_type = message_type
        self.__target = target
        self.__parameter = parameter
        self.__message = message

    @property
    def server(self) -> str:
        """The server the message originated from."""
        return self.__server

    @property
    def message_type(self) -> IRCControlMessageType:
        """The message type the message originated from."""
        return self.__message_type

    @property
    def target(self) -> str:
        """The message's target."""
        return self.__target

    @property
    def parameter(self) -> Optional[str]:
        """The message's parameter if set."""
        return self.__parameter

    @property
    def message(self) -> str:
        """The message itself."""
        return self.__message

    def __str__(self) -> str:
        """String representation of the message."""
        return ":{} {} {}{} {}".format(
            self.__server,
            self.__message_type.value,
            self.__target,
            " " + self.__parameter if self.__parameter else "",
            self.__message
        )

    @staticmethod
    def parse(line: str) -> Optional["IRCControlMessage"]:
        """Parse a message."""
        match = control_message_regex.match(line)
        if not match:
            return None

        server, raw_type, target, _, parameter, message = match.groups()
        try:
            message_type = IRCControlMessageType(raw_type)
        except ValueError:
            return None

        return IRCControlMessage(line, server, message_type, target, parameter, message)
