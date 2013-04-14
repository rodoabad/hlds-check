HLDS Check
==========

Sometimes even if a server is started with `-autoupdate` enabled it still tends to freeze. This is because the `-autoupdate` option will only restart the HLDS server upon a clean exit. So if you get something like `Segmentation fault (core dumped) $HL_CMD` then you're out of luck until someone manually restarts that server.

Requirements
------------

- Python 2.5+
- qstat 2.12+

HLDS Setup
----------

In order for this to work, you need to have your HLDS servers setup like this. Your HLDS directory should not contain any special characters or spaces. Replace your spaces with underscores.

You must start your HLDS server with *SCREEN* and it must have the same name as your HLDS directory.

```bash
screen -A -m -d -S server_1 ./hlds_run -game cstrike -maxplayers 32 +ip 127.0.0.1 +port 27015 +map de_dust2 +sys_ticrate 10000 +fps_max 1000 +sv_stats 1
```

How do I use it?
----------------
Configure `hlds_check.conf` first.

* **[main]** - This is where you setup your HLDS base directory through `base_dir`.
* **[servers]** - Add as many servers as you want as long as it follows the following format: `SCREEN name = ip:port`

The initial `hlds_check.conf` has some examples to help you start it up. Once you're done with the confi file, it's time to run `./hlds_check.py` for awesomeness.

Thanks
------

* TouchPad - For the initial Python build based on just my ideas. This is also the guy who asked me why I was using BASH instead of Python.