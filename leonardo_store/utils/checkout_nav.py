
def render_content(self, options):
    '''patch for render checkout nav'''
    request = options['request']

    if self.root:
        root = self.root
    else:
        root = self.parent

    try:
        fragments = options['request']._feincms_fragments
    except:
        fragments = {}

    checkout_nav = fragments.get("_current_brand", None)

    return self.render_response({
        'widget': self,
        'current': getattr(request, 'leonardo_page', None),
        'root': root,
        'level': self.level(root.level),
        'level2': self.level(root.level) + 1,
        'depth': self.depth,
        'request': request,
        'checkout_nav': checkout_nav
    })
