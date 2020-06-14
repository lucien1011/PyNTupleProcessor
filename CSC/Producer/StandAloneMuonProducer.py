from Core.Module import Module
from Core.Collection import Collection

n_max_segment = 11
n_chamber = 36
n_station = 4
n_ring = 4
n_endcap = 2

class StandAloneMuonProducer(Module):
    def analyze(self,event):
        event.standAloneMuons = [m for m in Collection(event,"muons") if m.isStandAloneMuon]
        for m in event.standAloneMuons:
            n_segment = len(m.cscSegmentRecord_endcap)
            m.segments_hash = []
            m.segments_localX = []
            m.segments_localY = []
            for i in range(n_segment):
                endcap = m.cscSegmentRecord_endcap[i]
                chamber = m.cscSegmentRecord_chamber[i]
                station = m.cscSegmentRecord_station[i]
                ring = m.cscSegmentRecord_ring[i]
                m.segments_hash.append(self.hash(chamber,station,ring,endcap)) 
                m.segments_localX.append(m.cscSegmentRecord_localX[i])
                m.segments_localY.append(m.cscSegmentRecord_localY[i])
            if len(m.segments_hash) < n_max_segment: m.segments_hash += [0]*(n_max_segment-len(m.segments_hash))
            if len(m.segments_localX) < n_max_segment: m.segments_localX += [0]*(n_max_segment-len(m.segments_localX))
            if len(m.segments_localY) < n_max_segment: m.segments_localY += [0]*(n_max_segment-len(m.segments_localY))
        return True

    def hash(self,chamber,station,ring,endcap):
        hash_endcap = (endcap-1)*n_chamber*n_station*n_ring
        hash_chamber = (chamber-1)*n_station*n_ring
        hash_station = (station-1)*n_ring
        hash_ring = ring-1
        return hash_endcap+hash_chamber+hash_station+hash_ring+1

