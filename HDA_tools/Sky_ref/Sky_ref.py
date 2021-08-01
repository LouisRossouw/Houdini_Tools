import hou

def Create(kwargs):
    """ function lets an object, instance to the spheres points, making for a temp sky refrence """

    node = kwargs['node']
    parm = kwargs['parm']
        
    obj = ('/obj')
    
    object = node.evalParm('object')
    
    sphere = node.createNode('sphere', 'sphere')
    box = node.createNode('box', 'box')
    grid =node.createNode('grid', 'grid')
        
    ref = node.createNode('sphere', 'ref')
    copyToPoints = node.createNode('copytopoints::2.0', 'ref')

    switch = node.createNode('switch', 'switch')    
    color = node.createNode('color', 'color')
    
    switch.setNextInput(sphere)   
    switch.setNextInput(box)
    switch.setNextInput(grid)

    color.setInput(0, switch)    
    copyToPoints.setInput(0, color)
    copyToPoints.setInput(1, ref)
    
    copyToPoints.setDisplayFlag(1)
    ref.parm('type').set(1)
    ref.parm('scale').set(100)
    ref.parm('freq').set(5)
    switch.parm('input').set(object)
    
    for n in node.children():
        n.moveToGoodPosition()


        
    
    
    
    
    
    