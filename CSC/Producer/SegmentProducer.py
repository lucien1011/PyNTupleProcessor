from Core.Module import Module
from Core.Collection import Collection

n_chamber = 36
n_station = 4
n_ring = 4
n_endcap = 2
n_channel = n_chamber*n_station*n_ring*n_endcap

class SegmentProducer(Module):
    def analyze(self,event):
        event.standAloneMuons = [m for m in Collection(event,"muons") if m.isStandAloneMuon]
        event.segment_localX = [0 for i in range(n_channel)]
        event.segment_localY = [0 for i in range(n_channel)]
        event.segment_muon = [0 for i in range(n_channel)]
        for im,m in enumerate(event.standAloneMuons):
            n_segment = len(m.cscSegmentRecord_endcap)
            for i in range(n_segment):
                endcap = m.cscSegmentRecord_endcap[i]
                chamber = m.cscSegmentRecord_chamber[i]
                station = m.cscSegmentRecord_station[i]
                ring = m.cscSegmentRecord_ring[i]
                hash = int(self.hash(chamber,station,ring,endcap))
                event.segment_localX[hash] = m.cscSegmentRecord_localX[i]
                event.segment_localX[hash] = m.cscSegmentRecord_localY[i]
                event.segment_muon[hash] = im            
        return True

    def hash(self,chamber,station,ring,endcap):
        hash_endcap = (endcap-1)*n_chamber*n_station*n_ring
        hash_chamber = (chamber-1)*n_station*n_ring
        hash_station = (station-1)*n_ring
        hash_ring = ring-1
        return hash_endcap+hash_chamber+hash_station+hash_ring+1

