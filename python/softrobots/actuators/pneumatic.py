def PneumaticCavity(node, name="pneumatic",
    cavityMeshFile, value=0, valueType="volumeGrowth"):
    
    """Creates and adds a pneumatic constraint.
    
    The constraint apply to a parent mesh.
    
    Args:
        cavityMeshFile (string): path to the cavity mesh (the mesh should be a surfacic mesh, ie only triangles or quads).
        
        value (real): value to apply, default is 0.
        
        valueType (string): type of the parameter value (volumeGrowth or pressure), default is volumeGrowth.
        
    Structure:
    .. sourcecode:: qml
        Node : {
                name : "pneumatic"
                MeshTopology,
                MechanicalObject,
                SurfacePressureConstraint,
                BarycentricMapping
        }
        
    """
    
    #  This create a new node in the scene. This node is appended to the finger's node.
    pneumatic = node.createChild(name)
    
    # This create a MeshTopology, a componant loading and holding the topology of the cavity.
    pneumatic.createObject('MeshTopology', name="topology", filename=cavityMeshFile)

    # This create a MechanicalObject, a componant holding the degree of freedom of our
    # mechanical modelling. In the case of a cavity actuated with pneumatic, it is a set of positions specifying
    # the points where the pressure is applied.
    pneumatic.createObject('MechanicalObject', src="@topology")

    # Create a SurfacePressureConstraint object with a name.
    # the indices are referring to the MechanicalObject's positions.
    # The last indice is where the pullPoint is connected.
    pneumatic.createObject('SurfacePressureConstraint',
                          value=value,
                          valueType=valueType)
                        
    # This create a BarycentricMapping. A BarycentricMapping is a key element as it will create a bi-directional link
    # between the cavity's DoFs and the parents's ones so that the pressure applied on the cavity wall will be mapped
    # to the volume structure and vice-versa;
    pneumatic.createObject('BarycentricMapping', name="mapping", mapForces="false", mapMasses="false")
    
    return pneumatic
    
def createScene(node):
    node.createObject('MechanicalObject')
    PneumaticCavity(node)