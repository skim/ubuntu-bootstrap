#!/usr/bin/env python
import bootstrap as bs

bs.sub("./00-info", echo=False)
bs.sub("./03-unmount", echo=False)
bs.sub("./05-create-filesystem", echo=False)
bs.sub("./10-mount", echo=False)
bs.sub("./20-debootstrap", echo=False)
bs.sub("./30-prepare", echo=False)
